# Generated by Django 3.1.7 on 2021-03-18 11:28

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testnobodypythpnbot', '0002_auto_20210311_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemID', models.IntegerField()),
                ('ProductName', models.CharField(max_length=50)),
                ('ProductPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Name', models.CharField(max_length=100)),
                ('Street', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=2)),
                ('ZipCode', models.CharField(max_length=5)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testnobodypythpnbot.telegramuser')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardID', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('ZipCode', models.CharField(max_length=10)),
                ('CardPan', models.CharField(max_length=100)),
                ('CVV', models.CharField(max_length=10)),
                ('Expiration', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Amount', models.CharField(max_length=20)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testnobodypythpnbot.telegramuser')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
