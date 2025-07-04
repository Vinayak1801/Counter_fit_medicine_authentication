# Generated by Django 5.1.6 on 2025-04-03 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bill_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('amount', models.FloatField()),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='dataset_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='order_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='product_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('manufactufre_date', models.DateField()),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='distributor_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('id_proof', models.FileField(upload_to='')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ORDER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.order_table')),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.product_table')),
            ],
        ),
        migrations.CreateModel(
            name='distributor_product_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('DISTRIBUTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.distributor_table')),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.product_table')),
            ],
        ),
        migrations.CreateModel(
            name='bil_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('BILL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.bill_table')),
                ('SHOP_PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.product_table')),
            ],
        ),
        migrations.CreateModel(
            name='request_from_distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('DISTRIBUTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.distributor_table')),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.product_table')),
            ],
        ),
        migrations.CreateModel(
            name='shop_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('owner_details', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='shop_product_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.distributor_product_table')),
                ('SHOP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.shop_table')),
            ],
        ),
        migrations.CreateModel(
            name='request_from_shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('DISTRIBUTOR_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.distributor_table')),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.product_table')),
                ('SHOP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.shop_table')),
            ],
        ),
        migrations.AddField(
            model_name='order_table',
            name='SHOP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.shop_table'),
        ),
        migrations.AddField(
            model_name='bill_table',
            name='SHOP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.shop_table'),
        ),
        migrations.CreateModel(
            name='stock_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.product_table')),
            ],
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='feedback_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('date', models.DateField()),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.product_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='complaint_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_App.user_table')),
            ],
        ),
    ]
