from flask import Blueprint, render_template, redirect, request, session, jsonify
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
    
    spotify_url = "https://api.spotify.com/v1/me/top/tracks"
    limit = 10
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
    returnable_data = []

    for item in fetched_data["items"]:
        track_data = {
            "id": fetched_data["items"]["id"],
            "name": fetched_data["items"]["name"],
            "image": fetched_data["items"]["album"]["images"][0]["url"] if item["album"]["images"] else None,
            "uri": fetched_data["items"]["uri"]
        }

        returnable_data.append(track_data)
    
    return jsonify(returnable_data)
