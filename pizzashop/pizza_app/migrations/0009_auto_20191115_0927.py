# Generated by Django 2.2.5 on 2019-11-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0008_auto_20191114_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='subtotal',
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=77.77, max_digits=50),
        ),
    ]
