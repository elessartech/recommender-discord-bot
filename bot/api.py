import os
import json
from dotenv import load_dotenv
from igdb.wrapper import IGDBWrapper

load_dotenv()
IGDB_API_TOKEN = os.getenv('IGDB_API_TOKEN')
IGDB_API_USER_ID = os.getenv('IGDB_API_USER_ID')

class IGDBAPIClient:
    def __init__(self):
        self.wrapper = IGDBWrapper(IGDB_API_USER_ID, IGDB_API_TOKEN)

    def get(self, category, criteria):
        try:
            result_in_bytes = self.wrapper.api_request(category, criteria)
            formatted_result = json.loads(result_in_bytes)
            return formatted_result
        except:
            raise Exception