# Modelos utilizados para esta prueba técnica
from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customers')
    sales_representative = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='customers',
        null=True,
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.company.name})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_birthday_display(self):
        if self.date_of_birth:
            return self.date_of_birth.strftime("%B %d")
        return "N/A"

class Interaction(models.Model):
    # Modelos utilizados: Company, Customer, Interaction
    INTERACTION_TYPES = [
        ('Call', 'Llamada'),
        ('Email', 'Correo Electrónico'),
        ('SMS', 'SMS'),
        ('Meeting', 'Reunión'),
        ('Whatsapp', 'WhatsApp'),
        ('Facebook', 'Facebook Messenger'),
        ('Twitter', 'Twitter DM'),
        ('LinkedIn', 'LinkedIn Message'),
        ('Other', 'Otro'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=50, choices=INTERACTION_TYPES)
    interaction_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-interaction_date']

    def __str__(self):
        return f"{self.interaction_type} with {self.customer.get_full_name()} on {self.interaction_date.strftime('%Y-%m-%d %H:%M')}"