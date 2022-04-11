import pandas as pd
import requests
import json
import googlemaps
from .config import settings


def find_nearby_theatres(addr):
    API_KEY = f'{settings.API_key}'
    map_client = googlemaps.Client(API_KEY)

    try:
        address = addr
        geocode = map_client.geocode(address=address)
        (lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))
        response = map_client.places_nearby(
            location=(lat, lng),
            keyword="theatre",
            type="movie",
            radius=5000
        )
        resp = response.get('results')
        return resp
    except:
        return pd.DataFrame
