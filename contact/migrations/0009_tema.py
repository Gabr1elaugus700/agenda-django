# Generated by Django 5.0.7 on 2024-08-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_aula_coach'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema_name', models.CharField(max_length=250)),
            ],
        ),
    ]