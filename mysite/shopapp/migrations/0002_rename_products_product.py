# Generated by Django 5.0.1 on 2024-04-26 20:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Products",
            new_name="Product",
        ),
    ]
