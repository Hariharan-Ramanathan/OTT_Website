# Generated by Django 2.2 on 2020-11-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0007_auto_20201106_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
