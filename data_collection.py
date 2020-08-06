# we are going to collect data about various restaurants in Paris 
# using the Yelp API

import requests 
import pandas as pd

api_key = 'your_api_key'

term = 'Restaurant'
location = 'Paris'
search_limit = 50
offset = 50

url = 'https://api.yelp.com/v3/businesses/search'

headers = {
    'Authorization': 'Bearer {}'.format(api_key),
}

df = pd.DataFrame()

for i in range(0, 951, 50):
    offset = 50
    offset += i 
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': search_limit,
        'offset': offset  
    }
    response = requests.get(url, headers=headers, params=url_params)
    print(response.json().keys())
    try:
        df_offset = pd.DataFrame.from_dict(response.json()['businesses'])
    except KeyError:
        print(response.json()['error'])
        continue
    df = df.append(df_offset)

print(df.shape)
print(df.head())

df.to_csv('data/restaurant_data.csv', index=False)


