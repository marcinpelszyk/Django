# Generated by Django 3.1.7 on 2021-05-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tax_rate',
            field=models.FloatField(choices=[(1, '23%'), (2, '8%'), (3, '5%'), (4, '0%')]),
        ),
    ]
