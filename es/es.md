# ElasticSearch
### 配置优化
- [ElasticSearch](https://pdai.tech/)
```shell
-XX:+UseConcMarkSweepGC
-XX:CMSInitiatingOccupancyFraction=75
-XX:+UseCMSInitiatingOccupancyOnly

-XX:+UseG1GC
-XX:MaxGCPauseMillis=50
```

- [sofa-jraft](https://www.5axxw.com/wiki/content/squ1cl)
- [DolphinScheduler教程](https://huaweicloud.csdn.net/63356355d3efff3090b5514d.html#font_colorpurple31__ExecutorControllerfont_103?login=from_csdn)

```shell
# https://kakawanyifan.com/11202
# ./elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.6.0/elasticsearch-analysis-ik-6.6.0.zip

GET /_cat/recovery/recovery-test?v&h=i,s,t,ty,st,snode,tnode,f,fp,b,bp


# IK分词器访问远程词典功能实现
# https://cloud.tencent.com/developer/article/1346943
# https://zhuanlan.zhihu.com/p/435407576?utm_id=0
GET /_analyze
{
  "text": ["中华人民共和国国歌"],
  "analyzer": "ik_max_word"
}

DELETE recovery-test

PUT /recovery-test
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  }
}

PUT /recovery-test/_settings
{
  "settings": {
    "number_of_replicas": 1
  }
}

PUT /recovery-test/_mapping
{
  "mappings": {
    "_doc": {
      "properties": {
        "id": {
          "type": "keyword"
        },
        "name": {
          "type": "text"
        },
        "age": {
          "type": "integer"
        },
        "bir": {
          "type": "date"
        }
      }
    }
  }
}

POST  recovery-test/_doc
{
  "name": "张三",
  "age": 30
}

GET recovery-test

GET /_cat/indices?v

# reindex
POST _reindex
{
  "source": {
    "index": "recovery-test"
  }, 
  "dest": {
    "index": "recovery-test-reindex"
  }
}

DELETE /recovery-test-reindex

PUT /recovery-test-reindex
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  }
}


GET _search
{
  "query": {
    "match_all": {
      
    }
  }
}
```