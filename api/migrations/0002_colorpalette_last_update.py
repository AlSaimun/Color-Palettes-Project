# Generated by Django 4.2.4 on 2023-08-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorpalette',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
    ]
