# Generated by Django 5.0.6 on 2024-07-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_market', '0004_alter_student_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='tutor_images'),
        ),
    ]
