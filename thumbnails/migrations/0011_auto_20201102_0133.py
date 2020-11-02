# Generated by Django 2.2 on 2020-11-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0010_thumbnail_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='genre',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER'), ('motivational', 'MOTIVATIONAL')], max_length=40),
        ),
    ]
