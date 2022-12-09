# Generated by Django 4.1.3 on 2022-12-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_orders_o_shippriority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='O_ORDERSTATUS',
            field=models.CharField(choices=[('1', '待支付'), ('2', '已支付')], default='1', help_text='订单状态', max_length=1, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='O_SHIPPRIORITY',
            field=models.IntegerField(choices=[(1, ' 一级'), (2, ' 二级'), (3, ' 三级'), (4, ' 四级')], default=1, help_text='运输优先级', verbose_name='运输优先级'),
        ),
    ]
