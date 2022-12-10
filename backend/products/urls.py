from django.urls import path

from . import views

# /products/
urlpatterns = [
    path('category-create/', views.CategoryCreate.as_view()),
    path('create/', views.ProductCreate.as_view()),
    path('', views.ProductListAll.as_view()),
    path('<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]
