# Generated by Django 5.0.6 on 2024-08-06 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_tutoringsession_subject'),
        ('tutor_market', '0020_tutor_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutoringsession',
            name='subject',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='tutor_market.subject'),
        ),
    ]
