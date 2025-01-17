# Generated by Django 2.2.7 on 2019-11-19 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.IntegerField(default=0)),
                ('background', models.CharField(default='', max_length=500)),
                ('geometry', models.CharField(default='', max_length=500)),
                ('glitchtype', models.CharField(default='', max_length=500)),
                ('audio', models.CharField(default='', max_length=500)),
                ('text', models.CharField(default='', max_length=500)),
                ('up_to', models.IntegerField(default=0)),
                ('down_to', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentChannel', models.IntegerField(default=0)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
