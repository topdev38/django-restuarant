# Generated by Django 3.1.7 on 2021-02-20 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('basemenu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='menu.basemenu')),
                ('percetage', models.IntegerField()),
                ('label', models.CharField(choices=[('RED', 'red'), ('BLUE', 'blue'), ('BLACK', 'black')], default='RED', max_length=5)),
            ],
            bases=('menu.basemenu',),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('basemenu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='menu.basemenu')),
                ('calorie', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menucategory')),
            ],
            bases=('menu.basemenu',),
        ),
    ]
