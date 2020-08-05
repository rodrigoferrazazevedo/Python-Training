import requests

urls = {
    'get': 'https://httpbin.org/get?title=rodrigo+ferraz+azevedo',
    'headers': 'https://httpbin.org/headers',
    'ip': 'https://httpbin.org/ip',
    'user-agent': 'https://httpbin.org/user-agent',
    'UUID': 'https://httpbin.org/uuid',
}

#'now': 'https://now.httpbin.org/', #deprecated

def get_content(title, url):
    resp = requests.get(url)
    print(f'Response for {title}')
    print(resp.json())

for title, url in urls.items():
    get_content(title, url)
    print('-' * 40)