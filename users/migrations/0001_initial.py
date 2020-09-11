# Generated by Django 3.1 on 2020-08-29 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=120)),
                ('country', models.CharField(choices=[('ru', 'Россия'), ('by', 'Беларусь')], default='by', max_length=20)),
                ('about', models.TextField(max_length=500)),
                ('tel1', models.CharField(max_length=25)),
                ('tel2', models.CharField(max_length=25)),
                ('email1', models.CharField(default='', max_length=25)),
                ('email2', models.CharField(default='', max_length=25)),
                ('fax', models.CharField(max_length=25)),
                ('adres1', models.CharField(max_length=150)),
                ('adres2', models.CharField(max_length=150)),
                ('inn', models.CharField(max_length=35)),
                ('website', models.URLField(blank=True, max_length=283, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]