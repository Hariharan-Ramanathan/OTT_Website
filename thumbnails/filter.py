import django_filters
from .models import *

CHOICE_FIELD=(
    ('HTL','High To Low'),
    ('LTH', 'Low To High')
)

class Moviefilter(django_filters.FilterSet):
    sort =  forms.ChoiceField(choices=CHOICE_FIELD)
    class Meta:
        model = thumbnail
        fields = ['language', 'genre']
    