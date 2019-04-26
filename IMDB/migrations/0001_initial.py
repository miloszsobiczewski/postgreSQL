# Generated by Django 2.1.8 on 2019-04-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True)),
                ('primary_name', models.CharField(max_length=100, unique=True)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
                ('death_year', models.IntegerField(blank=True, null=True)),
                ('primary_profession', models.CharField(max_length=100, unique=True)),
                ('known_for_titles', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True)),
                ('title_type', models.CharField(max_length=100, unique=True)),
                ('primary_title', models.CharField(max_length=100, unique=True)),
                ('original_title', models.CharField(max_length=100, unique=True)),
                ('is_adult', models.BooleanField()),
                ('start_year', models.IntegerField(blank=True, null=True)),
                ('end_year', models.IntegerField(blank=True, null=True)),
                ('runtime_minutes', models.IntegerField(blank=True, null=True)),
                ('genres', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
