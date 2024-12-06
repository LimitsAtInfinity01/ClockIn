# Generated by Django 5.1.4 on 2024-12-06 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clockInApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Admins",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name="employee",
            name="password",
        ),
        migrations.CreateModel(
            name="times",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timeIn", models.TimeField()),
                ("timeOut", models.TimeField()),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clockInApp.employee",
                    ),
                ),
            ],
        ),
    ]
