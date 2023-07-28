# Generated by Django 4.1.5 on 2023-07-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("Name", models.CharField(max_length=50)),
                ("Phone", models.CharField(max_length=50, unique=True)),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(max_length=50)),
                ("Company", models.CharField(max_length=50)),
            ],
        ),
    ]