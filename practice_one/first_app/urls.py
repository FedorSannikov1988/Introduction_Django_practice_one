from .views import index
from django.urls import path


urlpatterns = [
    path('hello_world', index, name='hello_world'),
]
