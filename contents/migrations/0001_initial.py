# Generated by Django 4.0.1 on 2022-01-28 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=10)),
                ('post_title', models.CharField(max_length=200)),
                ('post_category', models.CharField(max_length=200)),
                ('like_count', models.IntegerField()),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]