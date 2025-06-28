# Inserción de datos para la creación de datos por admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User 

from .models import Company, Customer, Interaction


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'company', 'sales_representative', 'date_of_birth', 'created_at')
    list_filter = ('company', 'sales_representative', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'company__name')
    date_hierarchy = 'date_of_birth' 

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'interaction_type', 'interaction_date', 'created_at')
    list_filter = ('interaction_type', 'interaction_date', 'customer__company', 'customer__sales_representative')
    search_fields = ('customer__first_name', 'customer__last_name', 'notes')
    date_hierarchy = 'interaction_date'