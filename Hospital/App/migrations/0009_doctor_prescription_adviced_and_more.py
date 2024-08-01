# Generated by Django 5.0.2 on 2024-02-29 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_doctor_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_prescription',
            name='adviced',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='doctor_prescription',
            name='provide',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='doctor_prescription',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.patient_appointment'),
        ),
        migrations.AlterField(
            model_name='doctor_prescription',
            name='prescription',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.CreateModel(
            name='medicine_distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(blank=True)),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.medical_shop')),
                ('patient', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='App.doctor_prescription')),
            ],
        ),
    ]
