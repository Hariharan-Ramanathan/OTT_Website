import django_filters
from django import forms
from .models import *

CHOICE_FIELD=(
    ('HTL','High To Low'),
    ('LTH', 'Low To High')
)

LANGUAGE_DROPDOWN=(
    ('tamil', 'TAMIL'),
    ('english', 'ENGLISH'),
    ('telugu', 'TELUGU'),
    ('hindi', 'HINDI'),
    ('malayalam', 'MALAYALAM'),
    ('urdhu', 'URDHU')
)

class Moviefilter(django_filters.FilterSet):
    class Meta:
        model = thumbnail
        fields = ['language', 'genre']
    