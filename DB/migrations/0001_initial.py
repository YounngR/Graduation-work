# Generated by Django 2.2.7 on 2020-05-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('h_Grade', models.CharField(blank=True, max_length=30, null=True)),
                ('h_Latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('h_Longitute', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('m_Code', models.CharField(blank=True, max_length=50, null=True)),
                ('m_Efficacy', models.CharField(blank=True, max_length=30, null=True)),
                ('m_Side_Effect', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]