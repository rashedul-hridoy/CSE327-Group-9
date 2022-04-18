# Generated by Django 3.2 on 2021-05-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_email', models.CharField(max_length=500)),
                ('doctor_password', models.CharField(max_length=500)),
                ('doctor_name', models.CharField(max_length=500)),
                ('doctor_gender', models.CharField(max_length=400)),
                ('doctor_visitng_hour', models.CharField(max_length=400)),
                ('doctor_room_number', models.CharField(max_length=400)),
            ],
        ),
    ]