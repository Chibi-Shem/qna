# Generated by Django 2.0.6 on 2018-06-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_confirmation_is_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmation',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]