# Generated by Django 2.2.3 on 2019-08-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20190821_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_no',
            field=models.CharField(db_index=True, default='fn-cdv1uxm7x', editable=False, max_length=100, unique=True),
        ),
    ]
