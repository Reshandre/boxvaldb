# Generated by Django 4.1.2 on 2023-02-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0002_alter_geographicalunit_geographicalunitcategory_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="Latitude",
            field=models.DecimalField(
                decimal_places=6,
                help_text="Latitude (parallel to equator):",
                max_digits=9,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="Longitude",
            field=models.DecimalField(
                decimal_places=6,
                help_text="Longitude (Through Nord and south Pole)):",
                max_digits=9,
                null=True,
            ),
        ),
    ]
