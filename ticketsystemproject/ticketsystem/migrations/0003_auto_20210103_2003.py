# Generated by Django 3.1.4 on 2021-01-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0002_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='files',
            field=models.FileField(null=True, upload_to='ticket_files'),
        ),
    ]