# Generated by Django 3.1.6 on 2023-03-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lcom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='descc',
            field=models.CharField(max_length=1800),
        ),
        migrations.AlterField(
            model_name='image',
            name='desccc',
            field=models.CharField(max_length=3000),
        ),
    ]
