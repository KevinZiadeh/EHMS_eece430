# Generated by Django 3.1.6 on 2021-04-11 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]