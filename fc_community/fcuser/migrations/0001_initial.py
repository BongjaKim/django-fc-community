# Generated by Django 3.0.3 on 2020-03-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fcuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='User Name')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='Resistered Time')),
            ],
        ),
    ]
