import requests

url = 'https://api.giphy.com/v1/gifs/search'
api_key = 'K7eDpg9GMVfuo1DMH9n0fgrDeM4koA2V'
search_string = 'cheeseburger'

params = {'q': search_string, 'api_key': api_key}

response = requests.get(url, params=params).json()

links = []

for link in range(1, 11):
    print(f'LINK #{link}: ', response['data'][link]['url'])
    links.append(response['data'][link]['url'])

print(links)
