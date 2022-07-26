# Generated by Django 4.0.3 on 2022-06-01 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0004_roomcustomization_price'),
        ('customer', '0012_hostelcustomer_room_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='designer.roomcustomization')),
            ],
        ),
    ]
