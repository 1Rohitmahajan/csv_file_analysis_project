# Generated by Django 5.0.7 on 2024-08-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysisApp', '0002_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
