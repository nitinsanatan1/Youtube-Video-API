from flask import Blueprint
from models.elastic_schema import *
from models.elastic_service import *

elastic_routes = Blueprint("elastic_routes",__name__)

# Elastic index creation route
@elastic_routes.get('/elastic/update_index_mapping')
def update_videos_index_mapping():
    return create_index()