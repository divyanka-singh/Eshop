# Generated by Django 4.1 on 2022-09-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Eshop", "0002_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="cat_image",
            field=models.ImageField(null=True, upload_to="upload/"),
        ),
    ]
