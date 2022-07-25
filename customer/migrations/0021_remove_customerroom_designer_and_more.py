# Generated by Django 4.0.3 on 2022-06-05 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_customerroom_designer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerroom',
            name='designer',
        ),
        migrations.RemoveField(
            model_name='customerroomcustomization',
            name='designer',
        ),
        migrations.AlterField(
            model_name='customerroom',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='customerroomcustomization',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
