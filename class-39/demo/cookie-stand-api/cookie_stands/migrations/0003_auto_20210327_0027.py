# Generated by Django 3.1.7 on 2021-03-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_stands', '0002_auto_20210327_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookiestand',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]