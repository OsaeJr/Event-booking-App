# Generated by Django 4.2.3 on 2023-08-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_events_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='Website Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.CharField(blank=True, max_length=50, verbose_name='Zip Code'),
        ),
    ]
