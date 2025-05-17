import json
import uuid
from datetime import datetime, timedelta

import jwt
import requests
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect

from chimera.settings import IPAAS_WORKSPACE_KEY, IPAAS_WORKSPACE_SECRET


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the chimera index.</h1>")

def empty_reponse(request):
    return JsonResponse({"status": "success"})


def add_action_page(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Add Action</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px auto;
                max-width: 600px;
                padding: 20px;
                background-color: #f5f5f5;
            }
        
            form {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
        
            div {
                margin-bottom: 15px;
            }
        
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
        
            input,
            textarea {
                width: 100%;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
        
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
        
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>"""
    csrf_token = get_token(request)
    html_form = f"""<body>
        <form method="POST" action="/api-action">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <div>
                <label for="integration_name">Integration Name:</label>
                <input type="text" id="integration_name" name="integration_name" required>
            </div>
            <div>
                <label for="entity_type">Entity Type:</label>
                <input type="text" id="entity_type" name="entity_type" required>
            </div>
            <div>
                <label for="entity_id">Entity Id:</label>
                <input type="text" id="entity_id" name="entity_id" required>
            </div>
            <div>
                <label for="object_id">Object Id:</label>
                <input type="text" id="object_id" name="object_id" required>
            </div>
            <div>
                <label for="note">Note:</label>
                <textarea id="note" name="note" rows="3" required></textarea>
            </div>
            <button type="submit">Submit Action</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html_content + html_form)


def add_action(request):
    """
    This view is used to add an action to the history.
    It will be called when the user submits the form.
    """
    # Get the form data from the request
    integration_name = request.POST.get("integration_name")
    entity_type = request.POST.get("entity_type")
    entity_id = request.POST.get("entity_id")
    object_id = request.POST.get("object_id")
    note = request.POST.get("note")
    timestamp = datetime.now().isoformat(timespec="seconds") + "Z"

    response = requests.post(
        url=f"https://api.integration.app/connections/{integration_name}/actions/add-activity/run",
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {get_customer_token(request.user)}",
        },
        json={
            "entity_type": entity_type,
            "entity_id": entity_id,
            "object_id": object_id,
            "note": note,
            "timestamp": timestamp,
        },
    )

    # Process the data as needed (e.g., save to database, etc.)
    # For demonstration purposes, we'll just return a simple response
    return HttpResponse(
        f"Action added. RESPONSE: {response.status_code} {response.text}"
    )


def get_customer_token(user):
    encoded_jwt = jwt.encode(
        {
            # ID of your customer in your system.
            # It will be used to identify customer in Integration.app
            "id": "6822d9a1a0df293732dde38e",
            # Human-readable name (it will simplify troubleshooting)
            "name": "Doniyor Rufatov",
            "iss": IPAAS_WORKSPACE_KEY,
            # Any customer fields you want to attach to your user.
            "fields": {},
            "exp": datetime.now() + timedelta(seconds=1440),
        },
        IPAAS_WORKSPACE_SECRET,
        algorithm="HS256",
    )
    return encoded_jwt


def get_authorization_url(request, integration_name):
    """
    This view is used to get the authorization URL for a specific integration.
    It will redirect the user to the authorization URL for the specified integration.
    """

    # For demonstration purposes, we'll just return a simple response

    token = get_customer_token(request.user)
    request_id = str(uuid.uuid4())

    redirect_url = (
        f"https://api.integration.app/connection-popup?"
        f"token={token}&requestId={request_id}&integrationKey={integration_name}"
    )

    return redirect(redirect_url)


def authorization_callback(request, integration_name):
    # get all request query params from request
    query_params = request.GET.dict()
    query_param_string = "&".join(
        [f"{key}={value}" for key, value in query_params.items()]
    )

    return redirect(f"https://api.integration.app/oauth-callback?{query_param_string}")
