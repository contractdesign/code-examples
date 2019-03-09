
In URLs below, base URL is IP_address:9200

# Store Data
                 POST /twitter/_doc message="this is a message" value:=1
                 PUT /twitter/_doc/2 message="this is a message" value:=1

# Mapping/Setting
                 GET /twitter/_mapping
                 GET /twitter/_mapping/_doc
                 GET /twitter/_settings

# Deletion
                 DELETE /twitter
                 DELETE /twitter/_doc
                 DELETE /twitter/_doc/

# Queries
All indices:     GET /_all/_search?q=tag:wow
Search all docs: GET /twitter/_doc/_search

[templates](http://mustache.github.io/mustache.5.html)
URI search:  	 GET /twitter/_doc/_search?user:kimchy

[Search ignoring TF/IDF](https://www.elastic.co/guide/en/elasticsearch/guide/current/ignoring-tfidf.html)

                 GET /_search
                 {
                   "query": {
                     "bool": {
                       "should": [
                         { "constant_score": {
                           "query": { "match": { "description": "wifi" }}
                         }}
                       ]
                     }
                   }
                 }
                 
Count            GET /twitter/_doc/_count?user:kimchy
Term Vectors:    GET /twitter/_doc/1/_termvectors
                 GET /twitter/_doc/1/_termvectors?fields=message

# Aggregations
Average:         POST /exams/_search?size=0
                 {
                     "aggs" : {
                         "avg_grade" : { "avg" : { "field" : "grade" } }
                     }
                 }

Other functions could be written with a [custom script](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-avg-aggregation.html)

# Analyzers: view how text is tokenized
                 GET /twitter/_analyze analyzer=standard text="this is a test"

[other analyzers](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-analyzers.html)


TODO 
- what is a shard?
- what is the difference between text and match?
- how to do a boolean search?
- experiment with shingle tokenizers
- what does the 'keyword' mean?


