import requests

USERS_URL = 'http://jsonplaceholder.typicode.com/users'
def get_users():
    """Get list of users"""
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None
