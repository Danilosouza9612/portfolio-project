# Generated by Django 2.0.2 on 2020-01-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200117_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='imagefun',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
