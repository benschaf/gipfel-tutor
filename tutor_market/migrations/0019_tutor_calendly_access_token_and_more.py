# Generated by Django 5.0.6 on 2024-07-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_market', '0018_alter_rating_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='calendly_access_token',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='calendly_refresh_token',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='calendly_token_expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
