# Generated by Django 4.0.1 on 2022-03-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_doctordetails_alter_admindetails_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetails',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
