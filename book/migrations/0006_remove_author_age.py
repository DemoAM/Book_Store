# Generated by Django 5.0.6 on 2024-06-17 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_author_name_alter_book_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='age',
        ),
    ]
