# Generated by Django 4.2.6 on 2023-11-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_alter_log_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
