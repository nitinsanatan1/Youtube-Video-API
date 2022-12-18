from flask import Blueprint
from flask import request as req
from services.api import *

# Youtube and Elastic services Routes
app_routes = Blueprint("app_routes",__name__)

@app_routes.get('/app/get_all_stored_videos')
def get_all_stored_videos():
    return get_all_videos_paginated()

@app_routes.get('/app/search_videos_by_keyword')
def get_videos_by_keyword():
    return get_videos_by_search_key(req.args.get('term'))

