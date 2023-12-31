# Generated by Django 4.2.6 on 2023-10-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="buildingData",
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
                ("buildingName", models.CharField(max_length=64)),
                ("hasElevator", models.BooleanField()),
                ("isElevatorWorking", models.BooleanField()),
                ("hasRamps", models.BooleanField()),
                ("numEntrances", models.PositiveSmallIntegerField()),
                ("numMotorizedEntrances", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
