# Generated by Django 2.2 on 2020-11-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0009_remove_thumbnail_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='genre',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER')], default=1, max_length=40),
            preserve_default=False,
        ),
    ]
