# Generated by Django 4.2.4 on 2023-08-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='x', max_length=200)),
                ('price', models.IntegerField()),
                ('color', models.CharField(blank=True, default='white', max_length=35)),
            ],
        ),
    ]
