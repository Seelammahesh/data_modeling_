# Generated by Django 4.2.4 on 2023-08-18 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('mobile_number', models.BigIntegerField()),
                ('dob', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('is_present', models.BooleanField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipkart.names')),
            ],
        ),
    ]
