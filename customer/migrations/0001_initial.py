# Generated by Django 4.0.3 on 2022-05-20 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20)),
                ('profile_pic', models.ImageField(upload_to='profile_pic/customer/')),
                ('date_of_birth', models.DateField(blank=True)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('check_in', models.DateField(blank=True)),
                ('duration', models.CharField(blank=True, max_length=40)),
                ('occupation', models.CharField(max_length=100)),
                ('work_place', models.CharField(blank=True, max_length=200)),
                ('profession', models.CharField(blank=True, max_length=400)),
                ('caste', models.CharField(blank=True, max_length=100)),
                ('contact_number', models.PositiveIntegerField(blank=True)),
                ('guardian_name', models.CharField(blank=True, max_length=400)),
                ('guardian_relation', models.CharField(blank=True, max_length=400)),
                ('guardian_contact_number', models.PositiveIntegerField(blank=True)),
                ('emergency_contact_number', models.PositiveIntegerField(blank=True)),
                ('permanent_address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=400)),
                ('state', models.CharField(blank=True, max_length=400)),
                ('pincode', models.PositiveIntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]