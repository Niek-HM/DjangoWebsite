# Generated by Django 3.2.6 on 2021-12-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211206_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpost',
            name='content',
            field=models.URLField(max_length=128, unique=True),
        ),
    ]
