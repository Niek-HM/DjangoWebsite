# Generated by Django 3.2.6 on 2021-11-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(upload_to='static/media/blog/'),
        ),
    ]
