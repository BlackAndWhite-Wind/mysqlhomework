# Generated by Django 4.1.3 on 2022-12-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_orders_o_shippriority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='O_ORDERPRIORITY',
            field=models.CharField(choices=[(1, ' 一级'), (2, ' 二级'), (3, ' 三级'), (4, ' 四级')], default='1', help_text='优先级', max_length=1, verbose_name='优先级'),
        ),
    ]
