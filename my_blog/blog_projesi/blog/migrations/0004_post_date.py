# Generated by Django 4.0.4 on 2022-05-18 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_parfume'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
