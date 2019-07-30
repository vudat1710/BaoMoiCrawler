from elasticsearch import Elasticsearch, helpers
import sys
import json
import os
import requests

res = requests.get('http://localhost:9200/')
# print (res.content)

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
count = 1

# with open("baomoicrawler/data.json", "r") as f:
#     data = f.read()
#     data = json.loads(data)

#     if (len(data) > 1):
#         for d in data:
#             res = es.index(index="baomoi", doc_type="json", id=count, body=d)
#             res = es.get(index="baomoi", doc_type="json", id=count)
#             count += 1
#     else:
#         res = es.index(index="baomoi", doc_type="json", id=count, body=data)
#         res = es.get(index="baomoi", doc_type="json", id=count)
#         count += 1

# es.indices.refresh(index="baomoi")

# res = es.search(index="baomoi", body={
#                 "query": {"multi_match": {"query": "Park Ji-sung"}}})
# res = es.search(index="baomoi", body={
#                 "query": {
#                     "multi_match": {
#                         "query": "Hà Nội", 
#                         "fields": ["title^3", "content"]
#                         }
#                     }
#                 })

res = es.search(index="baomoi", body={
                "query": {
                    "multi_match": {
                        "query": "Hà Nội", 
                        "type": "best_fields",
                        "fields": ["title^3", "content"],
                        "tie_breaker": 0.3
                        }
                    }
                })

print("%d documents found" % res['hits']['total']['value'])
for doc in res['hits']['hits']:
    print("%s %s" % (doc['_id'], doc['_source']['content']))
