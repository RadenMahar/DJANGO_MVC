# Generated by Django 2.2.3 on 2019-07-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RumahSakit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resep',
            name='total_harga',
            field=models.CharField(max_length=50),
        ),
    ]
