# Generated by Django 3.2.2 on 2021-05-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0, max_length=90),
        ),
    ]
