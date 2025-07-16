from datetime import datetime, timedelta
from django.views.decorators.http import require_GET, require_http_methods
import jwt
import requests
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from apps.connectors.base.resolver import (
    resolve_capability,
    resolve_capability_action,
    resolve_connector,
)

from chimera.settings import IPAAS_WORKSPACE_KEY, IPAAS_WORKSPACE_SECRET
from apps.connectors.base.global_actions import list_integrations as _list_integrations


def index(request):
    connector = resolve_connector("creatio")
    capability = connector.get_capability("entity")
    entities = capability.list_entities(
        dict(
            integration_key="creatio",
            identity={
                "id": "682200e11226bbc540e52a0a",
                "name": "Timur Kartaev",
            },
        )
    )
    schema = capability.get_entity_schema(
        dict(
            integration_key="creatio",
            entity_key="Opportunity",
            identity={
                "id": "682200e11226bbc540e52a0a",
                "name": "Timur Kartaev",
            },
        )
    )
    return JsonResponse(
        {
            "auth_url": "auth_url",
            "connectors": "connectors",
            "entities": entities,
            "schema": schema,
        }
    )


def run_action(request, integration_name):
    # connection_id 6829c429aab97852fdf3db34
    # https://api.integration.app/connections/{connectionSelector}/actions/{actionSelector}/run
    connection_id = "6829c429aab97852fdf3db34"

    query = request.GET.get("q")
    url = f"https://api.integration.app/connections/{integration_name}/actions/search-data-record/run"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_customer_token(request.user)}",
    }
    response = requests.post(
        url, headers=headers, json={"query": query, "entity_type": "deals"}
    )
    return JsonResponse({"response": response.json().get("output")})


def list_data_collections(request):
    connection_id = request.GET.get("connection_id", "")
    url = f"https://api.integration.app/connections/{connection_id}/data"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_customer_token(request.user)}",
    }
    response = requests.get(url, headers=headers)
    return JsonResponse({"entities": response.json()})


def get_data_collection_schema(request):
    connection_id = request.GET.get("connection_id", "682c61396ad656a84b8cbedd")
    data_collection_key = request.GET.get("entity_key", "deals")
    # import pdb; pdb.set_trace()
    url = f"https://api.integration.app/connections/{connection_id}/data/{data_collection_key}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_customer_token(request.user)}",
    }
    response = requests.get(url, headers=headers)
    return JsonResponse({"entity_schema": response.json()})


def list_data_sources(request):
    url = "https://api.integration.app/data-sources"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_customer_token(request.user)}",
    }
    response = requests.get(url, headers=headers)
    return JsonResponse({"response": response.json()})


def get_data_source(request):
    data_source_id = request.GET.get("data_source_id")
    url = f"https://api.integration.app/data-sources/{data_source_id}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_customer_token(request.user)}",
    }
    response = requests.get(url, headers=headers)
    return JsonResponse({"response": response.json()})


def list_connections(request):
    url = "https://api.integration.app/connections"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_customer_token(request.user)}",
    }
    response = requests.get(url, headers=headers)
    # print(response.json())
    # connections = [
    #     {'id': connection['id'], 'name': connection['name']}
    #     for connection in response.json().get('items', [])
    # ]
    return JsonResponse({"items": response.json().get("items", [])})


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
                <label for="title">Title:</label>
                <input type="text" id="title" name="title" required>
            </div>
            <div>
                <label for="document_name">Document Name:</label>
                <input type="text" id="document_name" name="document_name">
            </div>
            <div>
                <label for="document_link">Document Link:</label>
                <input type="url" id="document_link" name="document_link">
            </div>
            <div>
                <label for="document_id">Document ID:</label>
                <input type="text" id="document_id" name="document_id">
            </div>
            <div>
                <label for="status_from">Status From:</label>
                <input type="text" id="status_from" name="status_from">
            </div>
            <div>
                <label for="status_to">Status To:</label>
                <input type="text" id="status_to" name="status_to">
            </div>
            <div>
                <label for="changed_by">Changed By:</label>
                <input type="text" id="changed_by" name="changed_by">
            </div>
            <div>
                <label for="comment">Comment:</label>
                <textarea id="comment" name="comment" rows="3"></textarea>
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
    title = request.POST.get("title")
    document_name = request.POST.get("document_name")
    document_link = request.POST.get("document_link")
    document_id = request.POST.get("document_id")
    status_from = request.POST.get("status_from")
    status_to = request.POST.get("status_to")
    changed_by = request.POST.get("changed_by")
    comment = request.POST.get("comment")

    time_now = datetime.now()
    timestamp = time_now.timestamp()
    timestamp_str = time_now.isoformat(timespec="seconds") + "Z"

    def get_activity_html():
        return f"""
            <b>{title}</b><br>
            <b>Document:</b> <a href="{document_link}">{document_name}</a> <br>
            <b>Status Change:</b> {status_from} -&gt; <b>{status_to}</b> <br>
            <b>Changed By: </b>{changed_by} <br>
            <b>Date: </b> {timestamp_str} <br>
            <b>Comment:</b>&nbsp;<i>{comment}</i><br>
        """

    def get_activity_md():
        return (
            f"**{title}**\n"
            f"**Document:** [{document_name}]({document_link})\n"
            f"**Status Change:** {status_from} -&gt; **{status_to}**\n"
            f"**Changed By:** {changed_by}\n"
            f"**Date:** {timestamp_str}\n"
            f"**Comment:** *{comment}*"
        )

    response = requests.post(
        url=f"https://api.integration.app/connections/{integration_name}/actions/add-activity/run",
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {get_customer_token(request.user)}",
        },
        json={
            "timestamp": timestamp,
            "title": title,
            "document_name": document_name,
            "document_link": document_link,
            "document_id": document_id,
            "status_from": status_from,
            "status_to": status_to,
            "changed_by": changed_by,
            "comment": comment,
            "timestamp_date_str": timestamp_str,
            "activity_html_str": get_activity_html(),
            "activity_md_str": get_activity_md(),
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
            "id": "682200d25be10f8dedb486fa",
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


@require_GET
def info_list_integrations(request):
    response = _list_integrations(
        customer_id="682200e11226bbc540e52a0a",
        customer_name="Timur Kartaev",
    )
    return JsonResponse({"response": response})


@require_GET
def info_get_integration(request, integration_name):
    info = resolve_capability(integration_name, "info")
    response = info.get_integration(
        dict(
            customer_id="682200e11226bbc540e52a0a",
            customer_name="Timur Kartaev",
        )
    )
    return JsonResponse(response)


def archive_connection(request, connection_id):
    url = f"https://api.integration.app/connections/{connection_id}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_customer_token(request.user)}",
    }
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return JsonResponse({"status": "success"})


def gong_iframe(request):
    return render(request, "gong_iframe.html")


@require_GET
def authorization_begin(request, integration_name):
    connector = resolve_connector(integration_name)
    return JsonResponse(
        connector.authorize__begin(
            customer={
                "customer_id": "682200e11226bbc540e52a0a",
                "customer_name": "Timur Kartaev",
            }
        )
    )


@require_GET
@xframe_options_exempt
def authorization_finalize(request, integration_name):
    # get all request query params from request
    connector = resolve_connector(integration_name)
    query_params = request.GET.dict()
    result = connector.authorize__finalize(query_params=query_params)
    return render(request, "ipaas/auth_finalize.html", result)


@require_GET
def authorization_get_status(request, integration_name, request_id):
    result = resolve_capability_action(
        integration_name, "authorize", "get_auth_flow_status"
    )({"request_id": request_id})

    return JsonResponse(result)


@require_GET
def authorization_get_connection(request, integration_key):
    result = resolve_capability_action(integration_key, "authorize", "get_connection")(
        {
            "integration_key": integration_key,
            "identity": {
                "id": "682200e11226bbc540e52a0a",
                "name": "Timur Kartaev",
            },
        }
    )
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["DELETE"])
def authorize_disconnect_connection(request, integration_key, connection_id):
    result = resolve_capability_action(
        integration_key, "authorize", "disconnect_connection"
    )(
        {
            "connection_id": connection_id,
            "identity": {
                "id": "682200e11226bbc540e52a0a",
                "name": "Timur Kartaev",
            },
        }
    )
    return JsonResponse(result)


@require_GET
def entity_list_entities(request, integration_key):
    response = resolve_capability_action(integration_key, "entity", "list_entities")(
        dict(
            integration_key=integration_key,
            identity={
                "id": "682200e11226bbc540e52a0a",
                "name": "Timur Kartaev",
            },
        )
    )
    return JsonResponse(response)


@require_GET
def entity_get_entity_schema(request, integration_key, entity_key):
    response = resolve_capability_action(
        integration_key, "entity", "get_entity_schema"
    )(
        dict(
            integration_key=integration_key,
            entity_key=entity_key,
            identity={
                "id": "682200e11226bbc540e52a0a",
                "name": "Timur Kartaev",
            },
        )
    )
    return JsonResponse(response)


@require_GET
def object_list_objects(request, integration_key, entity_key):
    params = request.GET.dict()
    page = params.pop("page", None)
    extra_params = params
    response = resolve_capability_action(integration_key, "object", "list_objects")(
        dict(
            integration_key=integration_key,
            entity_key=entity_key,
            extra_params=extra_params,
            page=page,
            identity={
                "id": "682200e11226bbc540e52a0a",
                "name": "Timur Kartaev",
            },
        )
    )
    return JsonResponse(response)


@require_GET
def object_get_object(request, integration_key, entity_key, object_id):
    response = resolve_capability_action(integration_key, "object", "get_object")(
        dict(
            integration_key=integration_key,
            entity_key=entity_key,
            object_id=object_id,
            identity={
                "id": "682200e11226bbc540e52a0a",
                "name": "Timur Kartaev",
            },
        )
    )
    return JsonResponse(response)
