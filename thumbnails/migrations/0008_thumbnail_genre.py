# Generated by Django 2.2 on 2020-11-02 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0007_auto_20201102_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='genre',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER')], default=1, max_length=40),
            preserve_default=False,
        ),
    ]
