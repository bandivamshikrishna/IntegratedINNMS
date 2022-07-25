# Generated by Django 4.0.3 on 2022-06-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_pic', models.ImageField(upload_to='core/')),
                ('room_type', models.CharField(max_length=400)),
                ('room_fees', models.PositiveIntegerField()),
            ],
        ),
    ]
