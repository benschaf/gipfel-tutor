# Generated by Django 5.0.6 on 2024-07-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
