from celery import Celery

# celery config, using redis as broker and db
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'


# initialize celery app
def get_celery_app_instance(app):
    celery_beat_schedule = {
      "time_scheduler": {
          "task": "app.updating_youtube_data_with_celery",
          # Run this update task every 10 seconds
          "schedule": 10.0,
      }
    }

    celery = Celery(
        app.import_name,
        backend=CELERY_RESULT_BACKEND,
        broker=CELERY_BROKER_URL
    )
    
    celery.conf.update(app.config,
    beat_schedule=celery_beat_schedule)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery