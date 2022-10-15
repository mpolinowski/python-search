import requests
import json
from requests.auth import HTTPBasicAuth

from elastic_config import *

def ask_es(query):
    url = f'https://{elastic_url}/{elastic_index}/_search?q={query}'
    response = requests.get(url, auth = HTTPBasicAuth(elastic_user, elastic_pass), verify=False)
    result = response.content.decode()
    result_dictionary = json.loads(result)
    
    return result_dictionary

results = ask_es(query='Continuous%20Integration')

for result in results['hits']['hits']:
    print(result['_source']['title'])
    print(result['_source']['abstract'])