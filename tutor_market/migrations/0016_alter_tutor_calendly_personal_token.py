# Generated by Django 5.0.6 on 2024-07-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_market', '0015_tutor_calendly_event_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='calendly_personal_token',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
