# Generated by Django 4.0.3 on 2022-06-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0024_customerroomcustomization_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerroomcustomization',
            name='back',
            field=models.ImageField(null=True, upload_to='rooms/'),
        ),
        migrations.AddField(
            model_name='customerroomcustomization',
            name='bottom',
            field=models.ImageField(null=True, upload_to='rooms/'),
        ),
    ]
