# Generated by Django 5.0 on 2023-12-26 07:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_type', '0003_alter_fourwheelerparameter_company_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fourwheelerparameter',
            name='built_type',
        ),
        migrations.AddField(
            model_name='fourwheelerparameter',
            name='Fuel_Efficiency_Ratings',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='fourwheelerparameter',
            name='Performance_Ratings',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='fourwheelerparameter',
            name='Safety_Ratings',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='fourwheelerparameter',
            name='environment_safety',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]