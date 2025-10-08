from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet_hello, name='greet_hello'),
]