from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet_user, name='greet_user'),
]
