# Generated by Django 3.2.6 on 2021-11-22 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/media/'),
            preserve_default=False,
        ),
    ]
