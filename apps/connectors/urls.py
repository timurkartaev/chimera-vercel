from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from connectors import views

authorize_patterns = [
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
    re_path(
        r"^auth/(?P<integration_key>[-\w]+)/connection/?$",
        views.authorization_get_connection,
        name="authorize_get_connection",
    ),
    re_path(
        r"^auth/(?P<integration_key>[-\w]+)/connection/(?P<connection_id>[-\w]+)?$",
        views.authorize_disconnect_connection,
        name="authorize_disconnect_connection",
    ),
]

info_patterns = [
    re_path(
        r"^info/?$",
        views.info_list_integrations,
        name="info_list_integrations",
    ),
    re_path(
        r"^info/(?P<integration_name>[-\w]+)/?$",
        views.info_get_integration,
        name="info_get_integration",
    ),
]

entity_patterns = [
    re_path(
        r"^entity/(?P<integration_key>[-\w]+)/?$",
        views.entity_list_entities,
        name="entity_list_entities",
    ),
    re_path(
        r"^entity/(?P<integration_key>[-\w]+)/(?P<entity_key>[-\w]+)/?$",
        views.entity_get_entity_schema,
        name="entity_get_entity_schema",
    ),
]
urlpatterns = [
    *authorize_patterns,
    *info_patterns,
    *entity_patterns,
    path("", views.index, name="index-view"),
    path("add-history", views.add_action_page, name="add-history"),
    path("api-action", views.add_action, name="add-action"),
    path(
        "list-data-collections",
        views.list_data_collections,
        name="list-data-collections",
    ),
    path("list-integrations", views.info_list_integrations, name="list-integrations"),
    path("list-connections", views.list_connections, name="list-connections"),
    path("list-data-sources", views.list_data_sources, name="list-data-sources"),
    path("get-data-source", views.get_data_source, name="get-data-source"),
    path(
        "get-data-collection-schema",
        views.get_data_collection_schema,
        name="get-data-collection-schema",
    ),
    path("run-action/<str:integration_name>", views.run_action, name="run-action"),
    path(
        "archive-connection/<str:connection_id>",
        views.archive_connection,
        name="archive-connection",
    ),
    path("gong-iframe/", views.gong_iframe, name="gong_iframe"),  # keep this for now
]
