from django_filters import rest_framework as filters
from .models import Event

class EventFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    date = filters.DateFromToRangeFilter()
    location = filters.CharFilter(lookup_expr='icontains')
    organizer = filters.CharFilter(field_name='organizer__username', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'organizer']