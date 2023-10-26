# Generated by Django 4.1.1 on 2023-10-25 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='allusuarios',
            fields=[
                ('first_name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('username', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('cui', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('profile_image', models.ImageField(default='users_pictures/default.png', upload_to='Perfiles', verbose_name='Foto de Perfil')),
                ('login_attempts', models.IntegerField(default=0)),
                ('active_account', models.BooleanField(default=True)),
                ('account_locked', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universitario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'db_table': 'RegistrosEstudiantes',
                'ordering': ['cui'],
            },
        ),
    ]
