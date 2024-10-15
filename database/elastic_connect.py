from elasticsearch import Elasticsearch


elastic_client = Elasticsearch(
   ['http://localhost:9200'],
   basic_auth=("elastic", "7WB4MSv4"),
   verify_certs=False
)
