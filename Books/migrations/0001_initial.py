# Generated by Django 3.1.3 on 2020-12-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=120, unique=True)),
                ('price', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('author', models.CharField(max_length=120)),
            ],
        ),
    ]