# Generated by Django 2.2.3 on 2019-08-23 16:57

import airtech.helpers.id_generator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20190821_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_no',
            field=models.CharField(db_index=True, default=airtech.helpers.id_generator.id_gen, editable=False, max_length=100, unique=True),
        ),
    ]
