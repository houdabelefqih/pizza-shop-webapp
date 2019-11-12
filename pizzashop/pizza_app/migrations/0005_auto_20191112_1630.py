# Generated by Django 2.2.5 on 2019-11-12 16:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza_app', '0004_auto_20191107_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_app.Cart')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_app.Pizza')),
            ],
        ),
        migrations.DeleteModel(
            name='DinnerPlatters',
        ),
        migrations.DeleteModel(
            name='Pasta',
        ),
        migrations.DeleteModel(
            name='Salad',
        ),
        migrations.DeleteModel(
            name='Subs',
        ),
        migrations.AddField(
            model_name='customerorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='order_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]