from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from connectors import views

urlpatterns = [
    path("", views.index, name="index-view"),
    path("add-history", views.add_action_page, name="add-history"),
    path("api-action", views.add_action, name="add-action"),
    path("list-data-collections", views.list_data_collections, name="list-data-collections"),
    path("list-integrations", views.list_integrations, name="list-integrations"),
    path("list-connections", views.list_connections, name="list-connections"),
    path("list-data-sources", views.list_data_sources, name="list-data-sources"),
    path("get-data-source", views.get_data_source, name="get-data-source"),
    path("get-data-collection-schema", views.get_data_collection_schema, name="get-data-collection-schema"),
    path("run-action/<str:integration_name>", views.run_action, name="run-action"),
    path('archive-connection/<str:connection_id>', views.archive_connection, name="archive-connection"),
    # Authorize
    re_path(
        r"^auth/(?P<integration_name>[-\w]+)/begin/?$",
        views.authorization_begin,
        name="authorize_begin",
    ),
    re_path(
        r"^auth/(?P<integration_name>[-\w]+)/callback/?$",
        csrf_exempt(views.authorization_finalize),
        name="callback",
    ),
    re_path(
        r"^auth/(?P<integration_name>[-\w]+)/status/(?P<request_id>[-\w]+)?$",
        views.authorization_get_status,
        name="authorize_get_status",
    ),
]
