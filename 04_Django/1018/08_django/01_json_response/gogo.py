# gogo.py

import requests
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/json-3/') # 응답받아서
result = response.json() # json으로 변환

# pprint(result)
# pprint(result[0])
pprint(result[0].get('title'))
