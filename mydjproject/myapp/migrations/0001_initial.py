# Generated by Django 5.1.4 on 2024-12-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50, verbose_name='Name')),
                ('smobile', models.CharField(max_length=10, verbose_name='Mobile')),
                ('semail', models.CharField(max_length=50, verbose_name='Email')),
                ('spassword', models.CharField(max_length=50, verbose_name='Password')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
        ),
    ]
