# Generated by Django 4.0.3 on 2022-06-01 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0002_roomcustomization'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomcustomization',
            name='designer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='designer.designer'),
        ),
    ]
