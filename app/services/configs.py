import os
from dotenv import load_dotenv
load_dotenv()

# env secrets
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
CLOUD_ID = os.getenv('CLOUD_ID')
ELASTIC_API_KEY = os.getenv('ELASTIC_API_KEY')
YOUTUBE_VIDEOS_INDEX = os.getenv('YOUTUBE_VIDEOS_INDEX')