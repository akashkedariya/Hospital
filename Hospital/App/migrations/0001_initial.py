# Generated by Django 5.0.2 on 2024-02-16 09:20

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_detaile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=30, null=True)),
                ('mobile', models.BigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('blood_group', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('Specialties', models.CharField(choices=[('Neurologist', 'Neurologist'), ('Cardiologist', 'Cardiologist'), ('Surgeon', 'Surgeon'), ('Radiologist', 'Radiologist'), ('nurse', 'nurse'), ('other', 'other')], max_length=30, null=True)),
                ('degree', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('mobile', models.BigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('age', models.IntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=30, null=True)),
                ('doctor', models.BooleanField(default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('mobile', models.BigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('blood_group', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=30, null=True)),
                ('illnesses', models.CharField(max_length=500)),
                ('appoinment_date', models.DateField(default='', null=True)),
                ('appoinment_time', models.TimeField(blank=True, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.doctor_detaile')),
                ('patient_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]