# Generated by Django 5.0.2 on 2024-02-22 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_medical_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.CharField(max_length=500)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.patient_appointment')),
            ],
        ),
    ]
