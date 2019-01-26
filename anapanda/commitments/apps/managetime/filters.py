from .models import Task
import django_filters

# NOTE: this does not appear to be being called

class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Task
        fields = ['circle']
