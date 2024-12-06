# Generated by Django 5.1.4 on 2024-12-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("password", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "Employee",
            },
        ),
    ]