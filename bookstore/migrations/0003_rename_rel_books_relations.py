# Generated by Django 4.0.6 on 2022-07-16 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_books_rel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='rel',
            new_name='relations',
        ),
    ]
