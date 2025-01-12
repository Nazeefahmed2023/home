# Generated by Django 5.0.8 on 2024-11-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_alter_contact_desc_alter_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_json', models.CharField(max_length=5000)),
                ('amount', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=10)),
                ('zip_code', models.IntegerField(max_length=10)),
                ('oid', models.CharField(blank=True, max_length=50)),
                ('amountpaid', models.CharField(blank=True, max_length=50, null=True)),
                ('paymentstatus', models.CharField(default='', max_length=20)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('delivered', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
