# Generated by Django 2.2.5 on 2019-11-07 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0003_auto_20191107_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dinnerplatters',
            old_name='price',
            new_name='small_price',
        ),
        migrations.RenameField(
            model_name='pasta',
            old_name='price',
            new_name='small_price',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='price',
            new_name='small_price',
        ),
        migrations.RenameField(
            model_name='salad',
            old_name='price',
            new_name='small_price',
        ),
        migrations.RenameField(
            model_name='subs',
            old_name='price',
            new_name='small_price',
        ),
        migrations.RemoveField(
            model_name='dinnerplatters',
            name='item_size',
        ),
        migrations.RemoveField(
            model_name='pasta',
            name='item_size',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='item_size',
        ),
        migrations.RemoveField(
            model_name='salad',
            name='item_size',
        ),
        migrations.RemoveField(
            model_name='subs',
            name='item_size',
        ),
    ]
