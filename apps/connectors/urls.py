from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from connectors import views
from connectors.views import get_authorization_url, authorization_callback

urlpatterns = [
    path("", views.index, name="index-view"),
    # Authorize
    re_path(
        r"^auth/(?P<integration_name>[-\w]+)/begin/?$",
        get_authorization_url,
        name="authorize_begin",
    ),
    re_path(
        r"^auth/(?P<integration_name>[-\w]+)/callback/?$",
        csrf_exempt(authorization_callback),
        name="callback",
    ),
]
