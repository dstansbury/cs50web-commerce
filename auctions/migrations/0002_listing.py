# Generated by Django 3.2 on 2022-04-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('image', models.URLField()),
                ('condition', models.CharField(max_length=12)),
                ('description', models.TextField()),
                ('startPrice', models.DecimalField(decimal_places=2, max_digits=4)),
                ('currentPrice', models.DecimalField(decimal_places=2, max_digits=4)),
                ('duration', models.CharField(max_length=12)),
                ('remainingTime', models.DurationField()),
                ('listDate', models.DateTimeField()),
            ],
        ),
    ]
