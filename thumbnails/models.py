from django.db import models
from django.conf import settings    #user creation
from django import forms

User = settings.AUTH_USER_MODEL  #for user creation

GENRE_DROPDOWN = (
    ('action', 'ACTION'),
    ('comedy', 'COMEDY'),
    ('thriller', 'THRILLER'),
    ('motivational', 'MOTIVATIONAL')
)
class rating(models.Model):
    rate = models.IntegerField(null = True)

class thumbnail(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.FileField(blank=True, null=True)
    title = models.TextField(null = False)
    content = models.TextField(null=True)
    genre = models.CharField(max_length= 40, choices=GENRE_DROPDOWN)
    language = models.TextField(null = False)
    avg_rate = models.IntegerField(default = 0, null = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']      #for making last uploaded first

    