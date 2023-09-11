from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),  # Login page
    path('logout/', views.user_logout, name='logout'),  # Logout view
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
]
