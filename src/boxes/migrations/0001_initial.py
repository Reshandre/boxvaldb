# Generated by Django 4.1.4 on 2023-02-14 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("partners", "0001_initial"),
        ("assets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoxOccupied",
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
                ("Comments", models.TextField()),
                ("StartDay", models.DateField()),
                ("EndDay", models.DateField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "ForBox",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="assets.box"
                    ),
                ),
                (
                    "ForBusinessPartner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="partners.businesspartner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BoxReservationRequest",
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
                (
                    "ResevationStatus",
                    models.CharField(
                        choices=[
                            ("ReservationMade", "Reservation made"),
                            ("Agreed", "Agreed"),
                            ("Rejected", "Rejected"),
                            ("Requested", "Requested"),
                            ("Searching", "Searching"),
                        ],
                        default="Requested",
                        max_length=20,
                    ),
                ),
                ("comments", models.TextField()),
                ("StartDay", models.DateField()),
                ("EndDay", models.DateField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "ForBusinessPartner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="partners.businesspartner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BoxOccupiedLog",
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
                ("LogSequence", models.IntegerField()),
                (
                    "ForBoxOccupied",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="boxes.boxoccupied",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BoxConfirmedReservation",
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
                ("StartDay", models.DateField()),
                ("EndDay", models.DateField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "ForBox",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="assets.box"
                    ),
                ),
                (
                    "ForBusinessPartner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="partners.businesspartner",
                    ),
                ),
            ],
        ),
    ]