# Generated by Django 4.1 on 2022-09-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Eshop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="category",
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
                ("name", models.CharField(default="", max_length=100)),
            ],
        ),
    ]
