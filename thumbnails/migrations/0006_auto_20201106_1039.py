# Generated by Django 2.2 on 2020-11-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0005_auto_20201106_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='genre',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER'), ('motivational', 'MOTIVATIONAL'), ('love', 'LOVE')], max_length=40),
        ),
    ]
