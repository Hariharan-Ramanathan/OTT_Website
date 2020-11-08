from django.forms import TextInput, Textarea
from django.contrib import admin
from .models import thumbnail, rating
from django.db import models

class OTTAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
class thumbnail_admin(admin.ModelAdmin):
    list_display = ['__str__']
    class Meta:
        model = thumbnail

# Register your models here.

admin.site.register(thumbnail)
admin.site.register(rating)
