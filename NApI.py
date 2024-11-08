import requests
url='https://newsapi.org/v2/everything'
parms={
    'q':'India',
    'from':'2024-09-29',
    'apikey':'558bc6392f8146d291095ce5a5bd52a5',
    'pagesize':10
}
response=requests.get(url,params=parms)
data=response.json()
print(data)