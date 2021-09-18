from django.urls import path
from accounts.api import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.login_api_handler, name='login'),
    path('register/', views.register_api_handler, name='register'),
]