# Generated by Django 5.1 on 2024-09-19 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_remove_borrowbook_returned_books_returned_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='returned',
        ),
        migrations.AlterField(
            model_name='borrowbook',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 18, 17, 53, 36, 741393, tzinfo=datetime.timezone.utc)),
        ),
    ]
