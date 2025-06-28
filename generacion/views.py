# Logica de negocio para la vista de lista de clientes
from django.views.generic import ListView, TemplateView
from django.db.models import Max, F, Q, Subquery, OuterRef
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import ExtractMonth, ExtractDay

from .models import Customer, Interaction
class HomeView(TemplateView):
    template_name = 'generacion/home.html'

class CustomerListView(ListView):
    model = Customer
    template_name = 'generacion/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset().select_related('company', 'sales_representative')

        queryset = queryset.annotate(
            last_interaction_date=Max('interactions__interaction_date')
        )

        latest_interaction_for_customer = Interaction.objects.filter(
            customer=OuterRef('pk')
        ).order_by('-interaction_date', '-pk')

        queryset = queryset.annotate(
            last_interaction_type=Subquery(latest_interaction_for_customer.values('interaction_type')[:1])
        )

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(company__name__icontains=query)
            )

        birthday_filter = self.request.GET.get('birthday_this_week')
        if birthday_filter == 'true':
            today = timezone.now().date()
            start_of_week = today - timedelta(days=today.weekday())
            
            q_filter_birthday = Q()
            for i in range(7):
                date_in_week = start_of_week + timedelta(days=i)
                q_filter_birthday |= Q(
                    date_of_birth__month=date_in_week.month,
                    date_of_birth__day=date_in_week.day
                )
            queryset = queryset.filter(q_filter_birthday)

        order_by = self.request.GET.get('order_by', 'first_name')
        
        if order_by == 'company':
            queryset = queryset.order_by('company__name')
        elif order_by == 'birthday':
            queryset = queryset.annotate(
                birth_month=ExtractMonth('date_of_birth'),
                birth_day=ExtractDay('date_of_birth')
            ).order_by('birth_month', 'birth_day')
        elif order_by == 'last_interaction':
            queryset = queryset.order_by(F('last_interaction_date').desc(nulls_last=True))
        else:
            queryset = queryset.order_by(order_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for customer in context['customers']:
            if customer.last_interaction_date:
                time_diff = timezone.now() - customer.last_interaction_date
                if time_diff.days > 0:
                    customer.last_interaction_display = f"{time_diff.days} día{'s' if time_diff.days != 1 else ''} atrás ({customer.last_interaction_type or 'N/A'})"
                elif time_diff.seconds >= 3600:
                    hours = time_diff.seconds // 3600
                    customer.last_interaction_display = f"{hours} hora{'s' if hours != 1 else ''} atrás ({customer.last_interaction_type or 'N/A'})"
                elif time_diff.seconds >= 60:
                    minutes = time_diff.seconds // 60
                    customer.last_interaction_display = f"{minutes} minuto{'s' if minutes != 1 else ''} atrás ({customer.last_interaction_type or 'N/A'})"
                else:
                    customer.last_interaction_display = f"Justo ahora ({customer.last_interaction_type or 'N/A'})"
            else:
                customer.last_interaction_display = "Sin interacciones"
        return context