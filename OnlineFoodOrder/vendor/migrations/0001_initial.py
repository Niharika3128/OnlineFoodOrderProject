# Generated by Django 3.1 on 2020-09-02 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorRegistration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stall_name', models.CharField(max_length=50)),
                ('contact1', models.IntegerField(unique=True)),
                ('contact2', models.IntegerField()),
                ('stall_photo', models.ImageField(upload_to='stall_images/')),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=50)),
                ('otp', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('cuisine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.cuisinemodel')),
                ('stall_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.citymodel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodTypeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendorregistration')),
            ],
        ),
        migrations.CreateModel(
            name='FoodItemModel',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='food_items/')),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.foodtypemodel')),
            ],
        ),
    ]
