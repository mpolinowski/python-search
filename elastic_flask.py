from flask import Flask, render_template, request
import urllib.parse
import requests
import json

elastic_user = 'admin'
elastic_pass = 'admin'

def ask_elastic(query, elastic_url, elastic_index):
    url = f'https://{elastic_url}/{elastic_index}/_search?q={query}'
    response = requests.get(url, auth = requests.auth.HTTPBasicAuth(elastic_user, elastic_pass), verify=False)
    result = response.content.decode()
    result_dictionary = json.loads(result)
    
    return result_dictionary

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_get():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
    elastic_url = request.form['elastic_url']
    elastic_index = request.form['elastic_index']
    query = request.form['query']
    safe_request = urllib.parse.quote(query)
    # print(safe_request)
    response = ask_elastic(query=safe_request, elastic_url=elastic_url, elastic_index=elastic_index)
    results = response['hits']['hits']
    return render_template('results.html', query = query, len = len(results), result = results)

app.run(host='0.0.0.0') 
