# Generated by Django 2.2.7 on 2020-11-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0002_auto_20200624_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]