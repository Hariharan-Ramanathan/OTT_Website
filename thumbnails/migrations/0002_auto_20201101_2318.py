# Generated by Django 2.2 on 2020-11-01 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thumbnail',
            options={'ordering': ['-id']},
        ),
    ]
