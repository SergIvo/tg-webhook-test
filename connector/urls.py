from django.urls import path
from . import views


urlpatterns = [
    path('', views.redirect_from_index),
    path('echo', views.show_request_data, name='show_request_data'),
]
