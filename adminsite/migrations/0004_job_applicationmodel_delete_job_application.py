# Generated by Django 4.2.16 on 2024-09-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0003_job_application_alter_job_details_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_applicationmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=25)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='job_application',
        ),
    ]
