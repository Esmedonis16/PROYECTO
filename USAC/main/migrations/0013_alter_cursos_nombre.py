# Generated by Django 4.1.1 on 2023-10-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_cursos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
