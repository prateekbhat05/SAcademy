# Generated by Django 5.1 on 2024-09-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_register',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('highest_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('testid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tname', models.CharField(blank=True, max_length=200, null=True)),
                ('tdate', models.DateField(blank=True, null=True)),
                ('ttime', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
