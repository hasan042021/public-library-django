# Generated by Django 5.1 on 2024-09-19 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_borrowbook_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 18, 17, 26, 44, 181962, tzinfo=datetime.timezone.utc)),
        ),
    ]
