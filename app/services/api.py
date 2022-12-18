from time import time
from datetime import datetime
import googleapiclient.discovery
from services.configs import YOUTUBE_API_KEY,YOUTUBE_VIDEOS_INDEX
from models.elastic_service import *

# Get all video data stored in elastic search
def get_all_videos_paginated():
    all_videos = get_all_videos()
    page_size = 10
    paginated_response = {f'page_{i}': all_videos[i * page_size:(i + 1) * page_size] for i in range((len(all_videos) + page_size - 1) // page_size )}
    return paginated_response

# Search a keyword in db & find matching results.
# Fuzzy matches are also supported
def get_videos_by_search_key(term):
    video_results = get_search_results_by_term(term)
    return [video['_source'] for video in video_results]

# Request creator helper for Youtube_API
def create_request(pageToken=None):
    youtubeAPI = googleapiclient.discovery.build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtubeAPI.search().list(part="snippet",
        maxResults=50,
        q="cricket",
        order="date",
        pageToken=pageToken,
        publishedAfter= datetime.utcfromtimestamp((datetime.now().timestamp()) - 10).strftime("%Y-%m-%dT%H:%M:%S.0Z"))
                    
    return request

# Scrape videos data and Store results in db.
def get_youtube_results():
    t0 = time()
    youtube_request = create_request()

    video_count = 0
    docs = []

    # Loop ends if more than 5000 videos are scraped and stored, or next page doesn't exist
    while(video_count<5000):
        results = youtube_request.execute()
        video_count+=len(results['items'])

        if 'nextPageToken' in results:
            nextPageToken = results['nextPageToken']
        else:
            nextPageToken = None  
        
        if 'items' in results:
            for each_video in results['items']:
                docs.append({
                    "_index": YOUTUBE_VIDEOS_INDEX,
                    "_id": each_video['etag'],
                    "title": each_video['snippet']['title'],
                    "channelTitle": each_video['snippet']['channelTitle'],
                    "description": each_video['snippet']['description'],
                    "thumbnailUrls": each_video['snippet']['thumbnails']['default']['url'],
                    "publishedAt": each_video['snippet']['publishedAt']
                })
            
            # Update data on Elastic Index
            update_videos_on_elastic(docs)

        if nextPageToken:
            youtube_request = create_request(nextPageToken)
        else:
            break
               
    return "Data Successfully Updated: Process took {(time()-t0)/60} min(s)"