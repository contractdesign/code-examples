#!/usr/bin/env python3


from elasticsearch import Elasticsearch

es = Elasticsearch('localhost')

res = es.get(index='test', doc_type='hellowworld', id=1)

print(res)

