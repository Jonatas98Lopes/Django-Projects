# Generated by Django 4.1.7 on 2023-03-31 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0002_alter_investimentos_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investimentos',
            name='data',
            field=models.DateField(verbose_name=datetime.datetime.now),
        ),
    ]