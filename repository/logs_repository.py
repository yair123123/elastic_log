import logging
from datetime import datetime

from returns.result import Success, Failure

from database.elastic_connect import elastic_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


LOG_INDEX = "application_logs"

def setup_log_index():
   """Create log index with mapping"""
   if not elastic_client.indices.exists(index=LOG_INDEX):
       elastic_client.indices.create(index=LOG_INDEX, body={
           "mappings": {
               "properties": {
                   "timestamp": {"type": "date"},
                   "level": {"type": "keyword"},
                   "message": {"type": "text"},
                   "action": {"type": "keyword"}
               }
           }
       }
                                     )
def logger_write(level, message, action):

   """Log a message to both console and Elasticsearch"""
   log_entry = {
       "timestamp": datetime.now().isoformat(),
       "level": level,
       "message": message,
       "action": action
   }
   elastic_client.index(index=LOG_INDEX, body=log_entry)
   logger.log(level, f"{action}: {message}")