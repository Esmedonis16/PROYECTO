# Generated by Django 4.1.1 on 2023-10-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_allusuarios_cui'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusuarios',
            name='cui',
            field=models.CharField(default='0', max_length=13),
        ),
    ]