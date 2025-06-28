from django.urls import path
from .views import CustomerListView, HomeView

urlpatterns = [
    path('clientes/', CustomerListView.as_view(), name='customer_list'),
    path('home/', HomeView.as_view(), name='app_home'),
]