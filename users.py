import requests
import json

USERS_URL = 'http://jsonplaceholder.typicode.com/users'


def get_users():
    """Get list of users"""
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None


def get_user(user_id):
    """Get a single user using their ID"""
    all_users = get_users().json()
    for user in all_users:
        if user['id'] == user_id:
            return user
