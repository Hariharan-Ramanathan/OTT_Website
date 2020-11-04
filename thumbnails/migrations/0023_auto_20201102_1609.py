# Generated by Django 2.2 on 2020-11-02 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thumbnails', '0022_thumbnail_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='genre',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER'), ('motivational', 'MOTIVATIONAL')], default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='language',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]