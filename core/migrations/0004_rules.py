# Generated by Django 4.0.3 on 2022-06-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.TextField()),
            ],
        ),
    ]
