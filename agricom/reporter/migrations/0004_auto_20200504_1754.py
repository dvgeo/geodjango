# Generated by Django 2.0.5 on 2020-05-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0003_auto_20200504_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
