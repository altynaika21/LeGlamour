# Generated by Django 5.0.7 on 2024-08-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=123, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=123, null=True, verbose_name='Фамилия')),
                ('phone_number', models.CharField(max_length=17, unique=True, verbose_name='Номер телефона')),
                ('wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Баланс')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Обычный пользователь'), (2, 'Менеджер'), (3, 'Бухгалтер')], default=1, verbose_name='Статус пользователя')),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
