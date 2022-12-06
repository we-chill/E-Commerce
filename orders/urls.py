from django.urls import path

from . import views

# /orders/
urlpatterns = [
    path('', views.OrderListAPIView.as_view()),
    path('<int:pk>/', views.OrderDetailAPIView.as_view()),
    path('checkout/', views.checkout),
]
