# Generated by Django 5.0.6 on 2024-07-02 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OTP_code',
            new_name='OTPCode',
        ),
    ]
