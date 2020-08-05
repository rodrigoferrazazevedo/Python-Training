import requests

url = 'https://httpbin.org/post'
data = dict(title='Rodrigo Ferraz Azevedo')

resp = requests.post(url, data=data)
print('Response for POST')
print(resp.json())