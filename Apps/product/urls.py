from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('crear/', views.product_create, name='product_create'),
    path('editar/<int:pk>/', views.product_update, name='product_update'),
    path('eliminar/<int:pk>/', views.product_delete, name='product_delete'),
]