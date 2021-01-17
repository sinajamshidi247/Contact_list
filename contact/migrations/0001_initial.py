# Generated by Django 3.0 on 2021-01-17 16:04

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('realation', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
    ]
