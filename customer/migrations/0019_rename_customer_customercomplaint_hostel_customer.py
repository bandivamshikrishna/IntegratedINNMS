# Generated by Django 4.0.3 on 2022-06-04 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_alter_customercomplaint_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customercomplaint',
            old_name='customer',
            new_name='hostel_customer',
        ),
    ]