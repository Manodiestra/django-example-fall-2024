from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('hellouser', views.user_form, name='user_form'),
]
