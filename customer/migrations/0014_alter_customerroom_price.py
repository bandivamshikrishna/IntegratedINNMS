# Generated by Django 4.0.3 on 2022-06-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_customerroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerroom',
            name='price',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
