from django.urls import path
from .views import ProductAdminView
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('products/get/', views.product_get, name='product_get'),
]


urlpatterns += [
    path('admin/products/', ProductAdminView.as_view(), name='admin_product_add'),
    path('admin/products/<int:pk>/', ProductAdminView.as_view(), name='admin_product_delete'),
]
