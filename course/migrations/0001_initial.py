# Generated by Django 4.2.16 on 2024-09-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=10)),
                ('clanguage', models.CharField(max_length=10)),
                ('iname', models.CharField(max_length=10)),
                ('clevel', models.CharField(max_length=10)),
                ('ctime', models.CharField(max_length=10)),
                ('cdetails', models.CharField(max_length=10)),
                ('ccost', models.CharField(max_length=200)),
            ],
        ),
    ]
