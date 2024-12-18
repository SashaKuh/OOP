# Generated by Django 5.1.1 on 2024-10-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('anons', models.CharField(max_length=100, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('data', models.DateTimeField(verbose_name='Дата публікації')),
            ],
        ),
    ]
