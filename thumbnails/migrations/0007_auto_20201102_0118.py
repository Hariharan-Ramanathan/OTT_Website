# Generated by Django 2.2 on 2020-11-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0006_auto_20201102_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='title',
            field=models.TextField(),
        ),
    ]
