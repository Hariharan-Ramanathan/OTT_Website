# Generated by Django 2.2 on 2020-11-02 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0020_auto_20201102_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='avg_rate',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='language',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='title',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='user',
        ),
    ]
