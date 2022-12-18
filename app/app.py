from flask import Flask,jsonify
from services.api import *
from models.routes import elastic_routes
from services.routes import app_routes
from celery_worker import get_celery_app_instance

app = Flask(__name__)
celery = get_celery_app_instance(app)

# Registering blueprints of application logics
app.register_blueprint(elastic_routes)
app.register_blueprint(app_routes)

@app.route("/")
def home():
    return f"<h1> Welcome to Youtube-API! </h1>"

# celery task to get and update youtube videos data
@celery.task
def updating_youtube_data_with_celery():
    get_youtube_results()
    print("Task complete!")

# Route to redirect request to access youtube_api
@app.get('/app/get_data_from_youtube_api')
def update_youtube_results():
    updating_youtube_data_with_celery.delay()
    return f"Task triggered with Celery!"