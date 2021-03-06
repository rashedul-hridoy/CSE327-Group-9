# Generated by Django 3.2 on 2021-05-06 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_assistant_email', models.CharField(max_length=500)),
                ('doctor_assistant_password', models.CharField(max_length=500)),
                ('doctor_assistant_name', models.CharField(max_length=500)),
                ('doctor_assistant_gender', models.CharField(max_length=500)),
                ('doctor_assistant_age', models.IntegerField()),
                ('doctor_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
    ]
