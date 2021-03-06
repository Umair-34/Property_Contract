# Generated by Django 3.1 on 2021-03-22 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateField(blank=True, null=True)),
                ('ending_date', models.DateField(blank=True, null=True)),
                ('auto_renew', models.BooleanField(default=False)),
                ('rent_amount', models.IntegerField()),
                ('rent_due_date', models.DateField(blank=True, null=True)),
                ('deposit_amount', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '2 - Contract',
                'verbose_name_plural': '2 - Contracts',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=128, null=True)),
                ('property_type', models.CharField(blank=True, max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '1 - Property',
                'verbose_name_plural': '1 - Properties',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.contract')),
            ],
            options={
                'verbose_name': '3 - Payment',
                'verbose_name_plural': '3 - Payments',
            },
        ),
        migrations.AddField(
            model_name='contract',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.property'),
        ),
        migrations.AddField(
            model_name='contract',
            name='secondary_party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.person'),
        ),
    ]
