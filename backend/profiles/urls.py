from django.urls import path

from . import views

# /orders/
urlpatterns = [
    path('register/', views.RegisterUserAPIView.as_view()),
    path('logout/', views.BlackListTokenView.as_view()),
]
