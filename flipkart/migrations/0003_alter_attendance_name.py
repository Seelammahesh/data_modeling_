# Generated by Django 4.2.4 on 2023-08-18 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0002_alter_attendance_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipkart.names'),
        ),
    ]