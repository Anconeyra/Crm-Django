#Generación de datos de prueba

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from generacion.models import Company, Customer, Interaction
from faker import Faker
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Generates fake data for Users, Companies, Customers, and Interactions.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting fake data generation...'))
        fake = Faker('es_ES') # Usar Faker en español

        # 1. Crear representantes (Users)
        self.stdout.write('Creating 3 sales representatives...')
        sales_reps = []
        for i in range(1, 4):
            username = f'salesrep{i}'
            email = f'{username}@example.com'
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password('password123') # Contraseña simple para la prueba
                user.save()
                self.stdout.write(self.style.SUCCESS(f'  - Created user: {username}'))
            else:
                self.stdout.write(self.style.WARNING(f'  - User already exists: {username}'))
            sales_reps.append(user)
        self.stdout.write(self.style.SUCCESS('Sales representatives created.'))

        # 2. Crear Compañías (unas 10-15 para distribución)
        self.stdout.write('Creating companies...')
        companies = []
        num_companies = 15
        for _ in range(num_companies):
            company_name = fake.company()
            company, created = Company.objects.get_or_create(name=company_name)
            companies.append(company)
        self.stdout.write(self.style.SUCCESS(f'{len(companies)} companies created.'))

        # 3. Crear 1000 Clientes
        self.stdout.write('Creating 1000 customers...')
        customers = []
        for i in range(1000):
            first_name = fake.first_name()
            last_name = fake.last_name()
            company = random.choice(companies)
            sales_rep = random.choice(sales_reps)
            date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)

            customer = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                company=company,
                sales_representative=sales_rep,
                date_of_birth=date_of_birth
            )
            customers.append(customer)
            if (i + 1) % 100 == 0:
                self.stdout.write(f'  - {i+1} customers created...')
        self.stdout.write(self.style.SUCCESS('1000 customers created.'))

        # 4. Crear 500 Interacciones por Cliente (total ~500,000 interacciones)
        self.stdout.write('Creating interactions for each customer (500 per customer)...')
        interaction_types = [choice[0] for choice in Interaction.INTERACTION_TYPES]
        total_interactions = 0
        for i, customer in enumerate(customers):
            for _ in range(500):
                interaction_type = random.choice(interaction_types)
                # Fecha de interacción en los últimos 2 años
                interaction_date = fake.date_time_between(start_date='-2y', end_date='now')
                Interaction.objects.create(
                    customer=customer,
                    interaction_type=interaction_type,
                    interaction_date=interaction_date,
                    notes=fake.sentence() if random.random() > 0.5 else None # Notas opcionales
                )
                total_interactions += 1
            if (i + 1) % 100 == 0:
                self.stdout.write(f'  - Interactions for {i+1} customers created. Total: {total_interactions} interactions.')

        self.stdout.write(self.style.SUCCESS(f'Total {total_interactions} interactions created.'))
        self.stdout.write(self.style.SUCCESS('Fake data generation complete!'))