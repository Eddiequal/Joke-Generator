from django.urls import path
from .views import JokeView


urlpatterns = [
    path('api/jokes/', JokeView.as_view(), name='jokes'),
] 
