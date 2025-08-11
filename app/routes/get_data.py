from flask import Blueprint, render_template, redirect, request, session
from dotenv import load_dotenv
from urllib.parse import urlencode
import os
import requests
import base64
import pandas as pd

get_data_bp = Blueprint('get_data', __name__)
load_dotenv()

@get_data_bp.route('top-tracks')
def top_tracks():
    access_token = session.get("access_token")

    if not access_token:
        return redirect("/auth/login")
    
    spotify_url = " https://api.spotify.com/v1/me/top/tracks"
    limit = 50
    time_range = "long_term"

    headers = {
        "Authorization": "Bearer " + access_token
    }

    params = {
        "limit": limit,
        "time_range" : time_range
    }

    response = requests.get(spotify_url + "?" + urlencode(params), headers=headers)
    
    fetched_data = response.json()
    df = pd.DataFrame(fetched_data["items"])

    print(df)
    return fetched_data
