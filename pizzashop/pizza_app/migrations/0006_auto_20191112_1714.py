# Generated by Django 2.2.5 on 2019-11-12 17:14

from django.db import migrations, models
import rest_framework.compat


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0005_auto_20191112_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorder',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='toppings',
            field=models.ManyToManyField(to='pizza_app.Topping'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='max_toppings',
            field=models.PositiveSmallIntegerField(default=0, validators=[rest_framework.compat.MaxValueValidator(9)]),
        ),
    ]