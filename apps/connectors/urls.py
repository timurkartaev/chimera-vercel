from django.urls import path

from connectors import views

urlpatterns = [
    path('', views.index, name='index-view'),
]