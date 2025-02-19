# Generated by Django 5.1 on 2024-10-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0004_alter_property_main_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="location",
            field=models.CharField(
                choices=[("Oristano", "Oristano")], default="Oristano", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="property",
            name="property_type",
            field=models.CharField(
                choices=[("Bilocali", "Bilocali"), ("Trilocali", "Trilocali")],
                default="Trilocali",
                max_length=50,
            ),
        ),
    ]
