# Generated by Django 3.2 on 2021-05-01 18:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderID',
            field=models.UUIDField(default=uuid.uuid1),
        ),
    ]
