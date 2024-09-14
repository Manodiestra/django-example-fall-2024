from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_api, name='registration_api'),
    path('users/', views.user_list_api, name='user_list_api'),
]
