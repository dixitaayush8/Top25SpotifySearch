import numpy as np
import pandas as pd
import spotipy
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials(
        client_id='CLIENT_ID',
        client_secret='SECRET')

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

def getUserInput():
    someIn = str(raw_input('Search for anything on Spotify: '))
    return someIn

def playSearch():
    while True:
        pop = []
        name = []
        artists = []
        r = getUserInput()
        results = sp.search(q=r, limit=25) #searches for the string that the user inputs
        if(r.upper() == 'NO'):
            print('Enjoy your day')
            return False
        for i, t in enumerate(results['tracks']['items']): #appends the necessary data objects to the respective lists
            pop.append(t['popularity'])
            name.append(t['name'])
            artists.append(t['artists'][0]['name'])
        arrays = [np.array(name),np.array(artists)] #uses Numpy package to construct a MultiIndex of the song name and artist name
        ser = pd.Series(pop,index=arrays) #uses Pandas package to construct a Series, with the index being arrays
        serOrder = pd.Series.sort_values(ser,ascending=False) #creates an ordered series based on the populariy
        print serOrder

playSearch()