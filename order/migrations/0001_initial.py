# Generated by Django 3.1.7 on 2021-02-20 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(choices=[(1, 'TABLE 1'), (2, 'TABLE 2'), (3, 'TABLE 3'), (4, 'TABLE 4'), (5, 'TABLE 5')], default='TABLE 1', max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Alcohol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.alcohol')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.food')),
                ('order_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
