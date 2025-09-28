## importing django path and views
from django.urls import path
from . import views

## Django will set our website name as post_list
urlpatterns = [
    path('', views.post_list, name='post_list'),
]