# Generated by Django 3.1.4 on 2021-01-04 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0007_sharednews_datetime_shared'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharednews',
            old_name='image_url',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='sharednews',
            old_name='date',
            new_name='published_at',
        ),
    ]