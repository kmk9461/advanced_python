import os
from dotenv import load_dotenv
import requests
import pybase64

#before running this, make sure to create a .env file with your-client-id and your-client-secret 
#get these credentials here: https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token
load_dotenv()

#get credentials
your_client_id = os.environ.get("your-client-id")
your_client_secret = os.environ.get("your-client-secret")
credentials = f"{your_client_id}:{your_client_secret}"
credentials = pybase64.b64encode(credentials.encode())

#get access token
url = 'https://accounts.spotify.com/api/token'
token_data = {'grant_type':'client_credentials'}
headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization':f'Basic {credentials.decode()}'}
r = requests.post(url, data = token_data, headers=headers)
access_token = r.json()['access_token']

#get artist - Beyonce
artist_id = '6vWDO969PvNqNYHIOW5v0m'
url = f'https://api.spotify.com/v1/artists/{artist_id}'
headers = {'Authorization': f'Bearer {access_token}'}
r = requests.get(url, headers=headers)
print(r.text)

#get track - random track from tutorial
track_id = '56nmnMzaT44l8RmzPLkpdJ'
url = f'https://api.spotify.com/v1/'
r = requests.get(url + 'audio-features/' + track_id, headers=headers)
print(r.text)

# pull all artist's albums
r = requests.get(url + 'artists/' + artist_id + '/albums', 
                 headers=headers, 
                 params={'include_groups': 'album', 'limit': 50})
d = r.json()

#here are the different things we can pull from an album
print(d['items'][0].keys())
print([d['items'][i]['name'] for i in range(len(d['items']))])
print([d['items'][i]['release_date'] for i in range(len(d['items']))])
print([d['items'][i]['total_tracks'] for i in range(len(d['items']))])
