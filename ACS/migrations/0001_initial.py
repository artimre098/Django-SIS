# Generated by Django 5.0.2 on 2024-03-06 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountPayable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payable_id', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('due_date', models.CharField(max_length=50)),
                ('amount', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=50)),
                ('amount', models.BigIntegerField()),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('year_level', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount_paid', models.BigIntegerField()),
                ('receiver_user_id', models.CharField(max_length=20)),
                ('payment_date', models.CharField(max_length=50)),
                ('payable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACS.accountpayable')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACS.record')),
            ],
        ),
        migrations.CreateModel(
            name='Treasurer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ACS.record')),
            ],
        ),
        migrations.CreateModel(
            name='MoneyTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin_id', models.CharField(max_length=20)),
                ('amount_transferred', models.BigIntegerField()),
                ('date_transferred', models.CharField(max_length=50)),
                ('treasurer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACS.treasurer')),
            ],
        ),
    ]
