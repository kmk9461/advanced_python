import os
from dotenv import load_dotenv
import requests
import pybase64
import pandas as pd
import json

#before running this, must create a .env file with your-client-id and your-client-secret 
#get these credentials here: https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token
load_dotenv()

#get credentials and encode them
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
print('details we can pull about an artist')
print(r.text)
print('\n')

#get track - random track from tutorial
track_id = '56nmnMzaT44l8RmzPLkpdJ'
url = f'https://api.spotify.com/v1/'
r = requests.get(url + 'audio-features/' + track_id, headers=headers)
print('details we can pull about a track')
print(r.text)
print('\n')

# pull all artist's albums
r = requests.get(url + 'artists/' + artist_id + '/albums', 
                 headers=headers, 
                 params={'include_groups': 'album', 'limit': 50})
d = r.json()

#different things we can pull from an album
print('details we can pull about an album')
print(d['items'][0].keys())
print('album names:', [d['items'][i]['name'] for i in range(len(d['items']))])
print('release dates:', [d['items'][i]['release_date'] for i in range(len(d['items']))])
print('num of tracks:', [d['items'][i]['total_tracks'] for i in range(len(d['items']))])
print('\n')

# #get user defined playlist
url = f'https://api.spotify.com/v1/'
#this is me and a test playlist I made
r = requests.get(url + 'users/31ipbtu2v7pmtmja4r6i37rd6vrq/playlists/7qkgBK0HyIl7KGA0Z0wK7F', headers=headers)
d = r.json()
print('details we can pull about a playlist')
print(d.keys())
print('details we can pull about a track on a playlist')
print(d['tracks']['items'][0]['track'].keys())
print('\n')

print('playlist track #1')
print('track name:', d['tracks']['items'][0]['track']['name'])
print('popularity:', d['tracks']['items'][0]['track']['popularity'])
print('\n')

#we can pull the audio features of multiple tracks at once - max 100 though
track_ids = ",".join([d['tracks']['items'][i]['track']['id'] for i in range(len(d['tracks']['items']))])
url = f'https://api.spotify.com/v1/'
r = requests.get(url + 'audio-features?ids=' + track_ids, headers=headers)
res = json.loads(r.text)

#will need to merge back with the name etc