# Generated by Django 4.1.1 on 2022-09-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('PatientID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(blank=True, max_length=50, null=True)),
                ('LastName', models.CharField(blank=True, max_length=50, null=True)),
                ('DateOfBirth', models.DateField()),
                ('Sex', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]