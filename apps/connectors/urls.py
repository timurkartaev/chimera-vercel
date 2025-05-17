from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from connectors import views

urlpatterns = [
    path("", views.index, name="index-view"),
    path("add-history", views.add_action_page, name="add-history"),
    path("api-action", views.add_action, name="add-action"),
    path("empty-response", views.empty_reponse, name="simple-json-request"),
    # Authorize
    re_path(
        r"^auth/(?P<integration_name>[-\w]+)/begin/?$",
        views.get_authorization_url,
        name="authorize_begin",
    ),
    re_path(
        r"^auth/(?P<integration_name>[-\w]+)/callback/?$",
        csrf_exempt(views.authorization_callback),
        name="callback",
    ),
]
