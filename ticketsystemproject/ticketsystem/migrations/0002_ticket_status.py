# Generated by Django 3.1.4 on 2021-01-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('PD', 'Pending'), ('HA', 'Have answer'), ('CD', 'Closed')], default='PD', max_length=2),
        ),
    ]