# Generated by Django 4.1.5 on 2023-01-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universitycampus',
            name='campus_id',
        ),
        migrations.AddField(
            model_name='universitycampus',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
