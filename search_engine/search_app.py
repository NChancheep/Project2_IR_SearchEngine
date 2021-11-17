from flask import Flask, render_template, jsonify, request
from markupsafe import escape
from flask import render_template
from elasticsearch import Elasticsearch

import math

es = Elasticsearch()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    page_size = 10
    keyword = request.args.get('keyword')
    if request.args.get('page'):
        page_no = int(request.args.get('page'))
    else:
        page_no = 1
    body ={
        'size': page_size,
        'from': page_size*(page_no-1),
        'query': {
            'multi_match': {
                'query': keyword,
                'fields': ['anime_title','tags'],
                'fuzziness' : 'auto',
                'fuzzy_transpositions' : 'true'
            }
        }
    }
    res = es.search(index='anime_index', doc_type='',body=body)
    hits = [{'anime_title': doc['_source']['anime_title'],'anime_num_episodes': doc['_source']['anime_num_episodes'], 'anime_start_date_string': doc['_source']['anime_start_date_string'], 'anime_image_path': doc['_source']['anime_image_path'], 'tags': doc['_source']['tags']} for doc in res['hits']['hits']]
    page_total = math.ceil(res['hits']['total']['value']/page_size)
    total = res['hits']['total']['value']

    return render_template('search.html', keyword=keyword, hits=hits, page_no=page_no, page_total=page_total, total = total)