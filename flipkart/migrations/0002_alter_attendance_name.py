# Generated by Django 4.2.4 on 2023-08-18 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
