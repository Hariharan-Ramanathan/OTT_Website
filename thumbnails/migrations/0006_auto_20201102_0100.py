# Generated by Django 2.2 on 2020-11-02 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0005_thumbnail_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='title',
            field=models.TextField(max_length=30),
        ),
    ]