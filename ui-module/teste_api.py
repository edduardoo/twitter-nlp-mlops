import requests
from config import inf_api_key
  
url = 'https://p1r4dch4la.execute-api.us-east-1.amazonaws.com/prod'
  
inp = 18
params = {"Input": [inp]}
  
headers = {
        'Content-Type': 'application/json',
        'x-api-key': inf_api_key        
    }
  
response = requests.get(url, json=params, headers=headers)
  
data = response.json()
  
print(data)