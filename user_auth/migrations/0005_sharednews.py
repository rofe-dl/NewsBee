# Generated by Django 3.1.4 on 2021-01-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_auto_20210101_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('image_url', models.URLField(max_length=2048)),
                ('url', models.URLField(max_length=2048)),
                ('author', models.CharField(max_length=64)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('date', models.CharField(max_length=64)),
                ('user_profile', models.ManyToManyField(related_name='shared_news', to='user_auth.UserProfile')),
            ],
        ),
    ]