# Generated by Django 3.1.7 on 2021-02-20 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Alcohol',
            new_name='alcohol',
        ),
    ]
