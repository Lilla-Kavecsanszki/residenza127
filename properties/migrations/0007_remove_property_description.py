# Generated by Django 5.1 on 2024-10-21 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0006_property_is_sold"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="property",
            name="description",
        ),
    ]
