from elasticsearch import Elasticsearch, helpers
from time import time
from services.configs import CLOUD_ID, ELASTIC_API_KEY, YOUTUBE_VIDEOS_INDEX

# Elastic Client
es = Elasticsearch(
    cloud_id=CLOUD_ID,
    api_key=ELASTIC_API_KEY
)

# Bulk video update function
def update_videos_on_elastic(actions):
    return helpers.bulk(es,actions)

# Get all videos from elastic helper
def get_all_videos():
    search_query = {
        "query": {
            "match_all": {}
        },
        "size": 10000,
        "sort": [{
            "publishedAt": {
                "order": "desc"
            }
        }]
    }
    results = es.search(index=YOUTUBE_VIDEOS_INDEX, body=search_query)
    return results['hits']['hits']

# Get search query results from Elastic
def get_search_results_by_term(search_term):
    search_query = {
        "query": {
            "multi_match": {
                    "query": search_term,
                    "fields": ["title","channelTitle","description"]
                }
        },
        "size": 10,
        "sort": [{"publishedAt": {
            "order": "desc"
            }}
        ]
    }
    results = es.search(index=YOUTUBE_VIDEOS_INDEX, body=search_query)
    return results['hits']['hits']