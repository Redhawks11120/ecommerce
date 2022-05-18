# Generated by Django 4.0.3 on 2022-05-18 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_cart_item_remove_cart_quantity_cart_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='product.cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.item'),
        ),
    ]
