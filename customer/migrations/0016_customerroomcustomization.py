# Generated by Django 4.0.3 on 2022-06-01 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_alter_customerroom_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRoomCustomization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.ImageField(upload_to='rooms/')),
                ('right', models.ImageField(upload_to='rooms/')),
                ('top', models.ImageField(upload_to='rooms/')),
                ('front', models.ImageField(upload_to='rooms/')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]