# Generated by Django 5.1.4 on 2024-12-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clockInApp", "0002_admins_remove_employee_password_times"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="lastName",
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
