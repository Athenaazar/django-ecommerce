# Generated by Django 4.0.1 on 2022-02-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(blank=True, choices=[('', ''), ('out-of-stock', 'Hot'), ('new', 'New'), ('price-dec', 'Auction')], max_length=300, null=True),
        ),
    ]