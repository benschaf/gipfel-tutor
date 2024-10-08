# Generated by Django 5.0.6 on 2024-08-06 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_tutoringsession_session_status'),
        ('tutor_market', '0020_tutor_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoringsession',
            name='subject',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='tutor_market.subject'),
        ),
    ]
