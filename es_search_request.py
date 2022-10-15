import requests
from requests.auth import HTTPBasicAuth
import json

username = 'admin'
password = 'admin'

response = requests.get('https://localhost:9200/_search?q=Continuous%20Integration&filter_path=took,hits.hits._id,hits.hits._score,hits.hits._source&_source=title', auth = HTTPBasicAuth(username, password), verify=False)

result = response.content.decode()
print(type(result))

result_dictionary = json.loads(result)
print(type(result_dictionary))

best_match = result_dictionary['hits']['hits'][0]
print(best_match)