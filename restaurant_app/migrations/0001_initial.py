# Generated by Django 3.0 on 2020-07-04 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantModel',
            fields=[
                ('resto_id', models.AutoField(primary_key=True, serialize=False)),
                ('resto_name', models.CharField(max_length=30, unique=True)),
                ('resto_content', models.IntegerField(unique=True)),
                ('resto_email', models.EmailField(max_length=100, unique=True)),
                ('resto_password', models.CharField(max_length=30)),
                ('resto_otp', models.IntegerField()),
                ('resto_status', models.CharField(default=False, max_length=30)),
                ('resto_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.AreaModel')),
                ('resto_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.RestaurantTypeModel')),
            ],
        ),
    ]
