# Generated by Django 3.1 on 2021-03-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('condition', models.CharField(blank=True, max_length=128, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='Images/')),
            ],
            options={
                'verbose_name': '1 - InventoryItem',
                'verbose_name_plural': '1 - InventoryItems',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_value', models.IntegerField(blank=True, null=True)),
                ('inventory_items', models.ManyToManyField(to='inventory.InventoryItem')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.property')),
            ],
            options={
                'verbose_name': '2 - Inventory',
                'verbose_name_plural': '2 - Inventories',
            },
        ),
    ]
