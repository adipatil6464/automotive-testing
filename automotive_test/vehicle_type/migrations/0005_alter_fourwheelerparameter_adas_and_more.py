# Generated by Django 5.0 on 2024-01-14 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_type', '0004_remove_fourwheelerparameter_built_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourwheelerparameter',
            name='ADAS',
            field=models.CharField(choices=[('option1', 'Sedan'), ('option2', 'SUV'), ('option3', 'Pickup'), ('option4', 'Wagon'), ('option5', 'Minivan'), ('option6', 'Sports car'), ('option7', 'Utility vehicle'), ('option8', 'MPV'), ('option9', 'MUV'), ('option10', 'Van'), ('option11', 'Electric'), ('option12', 'Hybrid')], max_length=50),
        ),
        migrations.AlterField(
            model_name='fourwheelerparameter',
            name='passenger',
            field=models.IntegerField(max_length=50),
        ),
    ]