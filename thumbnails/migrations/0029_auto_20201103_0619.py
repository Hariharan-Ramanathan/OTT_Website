# Generated by Django 2.2 on 2020-11-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0028_auto_20201103_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
