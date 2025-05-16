import datetime
import uuid

import jwt
from django.http import HttpResponse
from django.shortcuts import redirect

from chimera.settings import IPAAS_WORKSPACE_KEY, IPAAS_WORKSPACE_SECRET


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the chimera index.</h1>")


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
            "exp": datetime.datetime.now() + datetime.timedelta(seconds=1440),
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
