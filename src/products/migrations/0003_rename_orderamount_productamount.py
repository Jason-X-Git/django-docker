# Generated by Django 3.2 on 2021-05-02 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210502_2120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderAmount',
            new_name='ProductAmount',
        ),
    ]
