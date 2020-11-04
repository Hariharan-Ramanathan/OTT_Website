import django_filters
from .models import *

class Moviefilter(django_filters.FilterSet):
    class Meta:
        model = thumbnail
        fields = ['language', 'genre']