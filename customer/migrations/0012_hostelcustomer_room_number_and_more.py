# Generated by Django 4.0.3 on 2022-06-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_hostelcustomer_total_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostelcustomer',
            name='room_number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hostelcustomer',
            name='duration',
            field=models.CharField(choices=[('3 months', '3 Months'), ('6 months', '6 Months'), ('9 months', '9 Months'), ('12 months', '12 Months'), ('more than 1 year', 'More than 1 Year')], max_length=40),
        ),
    ]