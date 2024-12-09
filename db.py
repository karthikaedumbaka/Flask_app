import json
import os

USER_DATA_FILE = 'users.json'


def read_users():
    """Reads users from the JSON file."""
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w') as file:
            json.dump({"users": []}, file)  # Initialize empty users list
    with open(USER_DATA_FILE, 'r') as file:
        return json.load(file)


def write_users(data):
    """Writes users to the JSON file."""
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def add_user(username, email, password):
    """Adds a new user to the database."""
    users_data = read_users()
    users = users_data.get('users', [])

    # Check if user already exists
    if any(user['username'] == username for user in users):
        return False

    # Add new user
    users.append({"username": username, "email": email, "password": password})
    users_data['users'] = users
    write_users(users_data)
    return True


def authenticate_user(username, password):
    """Authenticates a user by username and password."""
    users_data = read_users()
    users = users_data.get('users', [])

    return any(user for user in users if user['username'] == username and user['password'] == password)
