from django.urls import path
from .views import *
from app import views


urlpatterns = [
    path('', views.OrderView.as_view(), name='index_page'),
    path('process_cloth_data/', process_cloth_data, name='process_cloth_data'),
    path('order/<int:pk>/', views.DetailOrderView.as_view(), name='order_page'),
]
