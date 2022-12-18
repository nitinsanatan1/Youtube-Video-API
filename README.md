# Youtube-Video-API
## Steps to build this project
1. Clone this repository.
2. Add the `.env` file in the root path.
3. Run `docker-compose up -d --build` to build and launch project on docker.
4. After the project startup, one can access flask_app at `localhost:5001` 


## Tools used
1. Flask: Python based lightweight web-framework.
2. Redis: An in-memory data store & message broker. Used as a message broker and to store tasks.
3. Celery: Used to run and handle background tasks & schedule APIs too.
4. ElasticSearch: A lucene based, document search engine. Used as a db for fast retrival of data. 
5. Poetry: Dependency management and packaging tool.
6. Docker: To build containers.

## APIs
### Data APIs
1. To scrape data using Youtube_API async. every 10 seconds & store to ElasticSearch.
```
GET: /app/get_data_from_youtube_api
```
2. Get all stored videos data from elastic.
```
GET: /app/get_all_stored_videos
```
3. To search videos by specific terms. Supports fuzzy matching too.
```
GET: /app/search_videos_by_keyword?term=<search_keyword>
```

### Models APIs
1. To create a new elastic index using defined schema.
```
GET: /elastic/update_index_mapping
```
