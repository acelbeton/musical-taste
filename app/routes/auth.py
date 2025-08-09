from flask import Blueprint, render_template, redirect, request
from urllib.parse import urlencode
import secrets
import string
from dotenv import load_dotenv
import os
import requests
import base64

auth_bp = Blueprint('auth', __name__)
load_dotenv()

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
REDIRECT_URI = "http://127.0.0.1:5000/auth/callback"

@auth_bp.route('login')
def login():
    state = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))
    scope = 'user-read-private user-read-email'
    state_key = 'spotify_auth_state'

    params = {
        "response_type": "code",
        "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
        "scope": scope,
        "redirect_uri": REDIRECT_URI,
        "state": state
    }
    print(f"{SPOTIFY_AUTH_URL}?{urlencode(params)}")
    return redirect(f"{SPOTIFY_AUTH_URL}?{urlencode(params)}")

@auth_bp.route('callback')
def login_callback():
    code = request.args.get("code")
    print("Error:", request.args.get("error"))
    print("Code:", code)
    state = request.args.get("state")
    client_string = os.getenv("SPOTIFY_CLIENT_ID") + ':' + os.getenv("SPOTIFY_CLIENT_SECRET")
    client_string = client_string.encode('utf-8')
    client_string = base64.b64encode(client_string)

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + client_string.decode('utf-8')
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
        "client_secret": os.getenv("SPOTIFY_CLIENT_SECRET"),
        "redirect_uri": REDIRECT_URI,
    }

    response = requests.post(SPOTIFY_TOKEN_URL, data=token_data, headers=headers)

    return response.json()
    