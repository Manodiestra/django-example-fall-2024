from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_api, name='registration_api'),
    path('api/addUser/', views.AddUser.as_view(), name='add_user'),
    path('api/users/', views.user_list_api, name='user_list_api'),   # GET handler
]
