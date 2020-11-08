# Generated by Django 2.2 on 2020-11-05 10:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thumbnails', '0002_thumbnail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='user',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='rate', to=settings.AUTH_USER_MODEL),
        ),
    ]