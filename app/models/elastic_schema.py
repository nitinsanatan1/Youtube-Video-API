from models.elastic_service import es
from services.configs import YOUTUBE_VIDEOS_INDEX
from time import time

# Predefined mapping for elastic index
youtube_videos_index_mapping = {
    "mappings": {
        "properties": {
            "description": {
                "type": "text",
                "similarity": "BM25"
            },
            "channelTitle": {
                "type": "text",
                "similarity": "BM25"
            },
            "title": {
                "type": "text",
                "similarity": "BM25"
            },
            "thumbnailUrls": {
                "type": "keyword"
            },
            "publishedAt": {
                "type": "date"
            }
        }
    }
}

# Create a new index using a defined mapping on Elastic
def create_index():
    t0 = time()
    if es.indices.exists(YOUTUBE_VIDEOS_INDEX):
            es.indices.delete(YOUTUBE_VIDEOS_INDEX)
    es.indices.create(index=YOUTUBE_VIDEOS_INDEX, body=youtube_videos_index_mapping)
    return f"Success: Took {(time()-t0)/60} min(s)"