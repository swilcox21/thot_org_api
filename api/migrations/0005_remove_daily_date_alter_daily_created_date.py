# Generated by Django 4.1.4 on 2023-08-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_day_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily',
            name='date',
        ),
        migrations.AlterField(
            model_name='daily',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
