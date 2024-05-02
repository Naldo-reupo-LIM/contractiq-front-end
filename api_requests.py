from datetime import datetime

import requests

from constants import LOCAL_URL

REGISTER_URL = f"{LOCAL_URL}/register"
LOGIN_URL = f"{LOCAL_URL}/login"
PROJECTS_API_URL = f"{LOCAL_URL}/projects"
PROJECTS_API_URL_GET = f"{LOCAL_URL}/projects/user/"


def register_user(username, email, password):
    """
    Function to register a user by sending a POST request to the registration API.
    """
    # Get the current date
    join_date = datetime.now().strftime("%Y-%m-%d")

    # Make a POST request to the registration API
    data = {
        "user_name": username,
        "user_email_address": email,
        "join_date": join_date,
        "password": password,
    }
    response = requests.post(REGISTER_URL, json=data)
    return response


def authenticate_user(username, password):
    """
    Function to authenticate a user by sending a POST request to the login API.
    """
    data = {"user_email_address": username, "password": password}
    response = requests.post(LOGIN_URL, json=data)
    return response


def get_projects():
    """
    Function to get all workspaces by user.
    """

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    response = requests.get(PROJECTS_API_URL_GET, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data")
    return data


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzc5YTRjZGYtN2FkMy00MDI0LTg5NzAtM2E4NWM3ZDJlMDE5IiwiZXhwIjoxNzEzODc4NDY0fQ.9MagI_a1PIRXq6ADmUcVd6_LUTt_Wmc59OmJg-T1TOw"


def create_workspace(
    workspace_name,
    client_code,
    document_type,
    client_id,
    client_name,
    project_members,
    project_description,
):
    """
    Function to create a workspace by sending a POST request to the projects API.
    """
    payload = {
        "project_name": workspace_name,
        "document_type": document_type,
        "client_id": client_id,
        "project_members": project_members,
        "project_description": project_description,
        "client_code": client_code,
        "client_name": client_name,
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    response = requests.post(PROJECTS_API_URL, json=payload, headers=headers)

    return response


def create_next():

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    response = requests.post(PROJECTS_API_URL, headers=headers)

    return response
