# Generated by Django 2.2.6 on 2019-10-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('address', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=128)),
                ('website', models.CharField(max_length=128)),
            ],
        ),
    ]
