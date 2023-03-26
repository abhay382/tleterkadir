# Generated by Django 3.1.6 on 2023-03-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('tags', models.TextField()),
                ('img', models.FileField(upload_to='pic/%y/')),
                ('img2', models.FileField(upload_to='pict/%y/')),
                ('img3', models.FileField(upload_to='pictu/%y/')),
                ('img4', models.FileField(upload_to='pictur/%y/')),
                ('desc', models.CharField(max_length=300)),
                ('descc', models.CharField(max_length=1000)),
                ('desccc', models.CharField(max_length=1500)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
