# crm_project/urls.py

from django.contrib import admin
from django.urls import path, include 
from generacion.views import HomeView, CustomerListView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('admin/', admin.site.urls),
    path('', include('generacion.urls')), 
]