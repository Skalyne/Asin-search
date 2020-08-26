# Generated by Django 3.0.5 on 2020-08-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=8)),
                ('titulo', models.CharField(max_length=254)),
                ('bullet_1', models.CharField(max_length=254)),
                ('bullet_2', models.CharField(max_length=254)),
                ('bullet_3', models.CharField(max_length=254)),
                ('bullet_4', models.CharField(max_length=254)),
                ('bullet_5', models.CharField(max_length=254)),
                ('category', models.CharField(max_length=254)),
                ('query_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
