# Generated by Django 2.2 on 2020-11-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbnails', '0004_auto_20201105_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='language',
            field=models.CharField(choices=[('tamil', 'TAMIL'), ('english', 'ENGLISH'), ('telugu', 'TELUGU'), ('hindi', 'HINDI'), ('malayalam', 'MALAYALAM'), ('urdhu', 'URDHU')], max_length=30, null=True),
        ),
    ]
