from django.urls import path

from products.views import ProductDetailAPIView, ProductListAPIView

urlpatterns = [
    path('categories/<int:types_id>/list/', ProductListAPIView.as_view(), name='ProductList'),
    path('categories/<int:pk>/', ProductDetailAPIView.as_view(), name='ProductDetail'),
]