# Generated by Django 2.2 on 2020-11-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0035_auto_20201104_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]