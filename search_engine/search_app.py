from flask import Flask
from markupsafe import escape
from flask import render_template
from elasticsearch import Elasticsearch

es = Elasticsearch()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    body ={
        'size':10,
        'query':{
            'match_all':{}
        }
    }
    res = es.search(index='anime_index',doc_type='',body=body)
    return render_template('search.html',result=res)
