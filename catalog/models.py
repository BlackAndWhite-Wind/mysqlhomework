from django.db import models


# Create your models here.

class Admin(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    class Meta:
        verbose_name = verbose_name_plural = "管理员"

    def __str__(self):
        return self.username


class REGION(models.Model):  # 地区表
    R_REGIONKEY = models.IntegerField(primary_key=True, verbose_name="地区代码", help_text="地区代码，主键")
    R_NAME = models.CharField(max_length=25, verbose_name="地区名称", help_text="地区名称")
    R_COMMENT = models.TextField(max_length=152, verbose_name="评价", help_text="评价")
    PS_SUPPLYCOST = models.FloatField(verbose_name="供应价格", help_text="供应价格")
    PS_COMMENT = models.TextField(max_length=199, verbose_name="备注", help_text="备注")

    class Meta:
        verbose_name = verbose_name_plural = "地区"

    def __str__(self):
        return self.R_NAME

    # def get_absolute_url(self):
    #     return reverse('region-detail', args=[str(self.R_REGIONKEY)])


class NATION(models.Model):  # 国家表
    N_NATIONKEY = models.IntegerField(primary_key=True, verbose_name="国家代码", help_text="国家代码，主键")
    N_NAME = models.CharField(max_length=25, verbose_name="国家名称", help_text="国家名称")
    N_REGIONKEY = models.ForeignKey(to="REGION", to_field="R_REGIONKEY", related_name="NR_REGIONKEY",
                                    on_delete=models.SET_NULL, null=True, help_text="所属地区,外键R_REGIONKEY",
                                    verbose_name="所属地区")
    N_COMMENT = models.TextField(max_length=199, verbose_name="备注", help_text="备注")

    class Meta:
        verbose_name = verbose_name_plural = "国家"

    def __str__(self):
        return self.N_NAME

    # def get_absolute_url(self):
    #     return reverse('region-detail', args=[str(self.R_REGIONKEY)])


class CUSTOMER(models.Model):  # 顾客表
    C_CUSTKEY = models.IntegerField(primary_key=True, verbose_name="顾客编号", help_text="顾客编号，主键")
    C_NAME = models.CharField(max_length=25, verbose_name="顾客名称", help_text="顾客名称")
    C_ADDRESS = models.CharField(max_length=40, verbose_name="顾客地址", help_text="顾客地址")
    C_NATIONKEY = models.ForeignKey(to="NATION", to_field="N_NATIONKEY", related_name="CN_NATIONKEY",
                                    on_delete=models.SET_NULL, null=True, help_text="所属国家,外键N_NATIONKEY",
                                    verbose_name="所属国家")
    C_PHONE = models.CharField(max_length=15, verbose_name="联系电话", help_text="联系电话")
    C_ACCTBAL = models.FloatField(verbose_name="可用余额", help_text="可用余额")
    C_MKTSEGMENT = models.CharField(max_length=10, verbose_name="市场", help_text="市场")
    C_COMMENT = models.TextField(max_length=117, verbose_name="备注", help_text="备注")

    class Meta:
        verbose_name = verbose_name_plural = "顾客"

    def __str__(self):
        return self.C_NAME

    # def get_absolute_url(self):
    #     return reverse('region-detail', args=[str(self.R_REGIONKEY)])


class PART(models.Model):  # 零件表
    P_PARTKEY = models.IntegerField(primary_key=True, verbose_name="零件编号", help_text="零件编号，主键")
    P_NAME = models.CharField(max_length=55, verbose_name="零件名称", help_text="零件名称")
    P_MFGR = models.CharField(max_length=25, verbose_name="生产商", help_text="生产商")
    P_BRAND = models.CharField(max_length=10, verbose_name="品牌", help_text="品牌")
    P_TYPE = models.CharField(max_length=10, verbose_name="型号", help_text="型号")
    P_SIZE = models.IntegerField(verbose_name="尺寸", help_text="尺寸")
    P_CONTAINER = models.CharField(max_length=10, verbose_name="包装容器", help_text="包装容器")
    P_RETAILPRICE = models.FloatField(verbose_name="零售价", help_text="零售价")
    P_COMMENT = models.TextField(max_length=23, verbose_name="备注", help_text="备注")

    class Meta:
        verbose_name = verbose_name_plural = "零件"

    def __str__(self):
        return self.P_NAME

    # def get_absolute_url(self):
    #     return reverse('region-detail', args=[str(self.R_REGIONKEY)])   


class SUPPLIER(models.Model):  # 供应商表
    S_SUPPKEY = models.IntegerField(primary_key=True, verbose_name="供应商编号", help_text="供应商编号，主键")
    S_NAME = models.CharField(max_length=55, verbose_name="供应商名称", help_text="供应商名称")
    S_ADDRESS = models.CharField(max_length=40, verbose_name="供应商地址", help_text="供应商地址")
    S_NATIONKEY = models.ForeignKey(to="NATION", to_field="N_NATIONKEY", related_name="SN_NATIONKEY",
                                    on_delete=models.SET_NULL, null=True, help_text="所属国家,外键N_NATIONKEY",
                                    verbose_name="所属国家")
    S_PHONE = models.CharField(max_length=15, verbose_name="电话", help_text="电话")
    S_ACCTBAL = models.FloatField(verbose_name="余额", help_text="余额")
    S_COMMENT = models.TextField(max_length=101, verbose_name="备注", help_text="备注")

    class Meta:
        verbose_name = verbose_name_plural = "供应商"

    def __str__(self):
        return self.S_NAME

    # def get_absolute_url(self):
    #     return reverse('region-detail', args=[str(self.R_REGIONKEY)])   


class PARTSUPP(models.Model):  # 零件供应表
    PS_PARTKEY = models.OneToOneField(to="PART", to_field="P_PARTKEY", related_name="PSP_PARTKEY",
                                      on_delete=models.SET_NULL, null=True,
                                      help_text="零件名称,外键P_PARTKEY。与PS_SUPPKEY联合构成主键",
                                      verbose_name="零件编号")
    PS_SUPPKEY = models.OneToOneField(to="SUPPLIER", to_field="S_SUPPKEY", related_name="PSS_SUPPKEY",
                                      on_delete=models.SET_NULL, null=True, help_text="供应商名称,外键S_SUPPKEY",
                                      verbose_name="供应商编号")
    PS_AVAILQTY = models.FloatField(verbose_name="供应数量", help_text="供应数量")
    PS_SUPPLYCOST = models.FloatField(verbose_name="供应价格", help_text="供应价格")
    PS_COMMENT = models.TextField(max_length=199, verbose_name="备注", help_text="备注")

    class Meta:
        unique_together = ("PS_PARTKEY", "PS_SUPPKEY")
        verbose_name = verbose_name_plural = "零件供应"

    def __str__(self):
        return f"{self.PS_PARTKEY},{self.PS_SUPPKEY}"

    # def get_absolute_url(self):
    #     return reverse('region-detail', args=[str(self.R_REGIONKEY)])  


class ORDERS(models.Model):  # 订单表
    O_ORDERKEY = models.IntegerField(primary_key=True, verbose_name="订单编号", help_text="订单编号，主键")
    O_CUSTKEY = models.ForeignKey(to="CUSTOMER", to_field="C_CUSTKEY", related_name="OC_CUSTKEY",
                                  on_delete=models.SET_NULL, null=True, help_text="顾客名称,外键C_CUSTKEY",
                                  verbose_name="顾客名称")
    status_choices = (
        ('1', '待支付'),
        ('2', '已支付'),
    )
    O_ORDERSTATUS = models.CharField(max_length=1, verbose_name="订单状态", help_text="订单状态",
                                     choices=status_choices, default='1')
    O_TOTALPRICE = models.FloatField(verbose_name="订单金额", help_text="订单金额", default=0)
    O_ORDERDATE = models.DateField(verbose_name="订单日期", help_text="订单日期")
    status_choices_2 = (
        ('1', ' 一级'),
        ('2', ' 二级'),
        ('3', ' 三级'),
        ('4', ' 四级'),
    )
    O_ORDERPRIORITY = models.CharField(max_length=1, verbose_name="优先级", help_text="优先级",
                                       choices=status_choices_2, default='1')
    O_CLERK = models.CharField(max_length=15, verbose_name="制单员", help_text="制单员")
    O_SHIPPRIORITY = models.CharField(max_length=1, verbose_name="运输优先级", help_text="运输优先级",
                                      choices=status_choices_2, default='1')
    O_COMMENT = models.TextField(max_length=79, verbose_name="备注", help_text="备注")

    class Meta:
        verbose_name = verbose_name_plural = "订单"

    def __str__(self):
        return str(self.O_ORDERKEY)

    # def get_absolute_url(self):
    #     return reverse('region-detail', args=[str(self.R_REGIONKEY)])  


class LINEITEM(models.Model):  # 订单明细表
    L_ORDERKEY = models.OneToOneField(to="ORDERS", to_field="O_ORDERKEY", related_name="LO_ORDERKEY",
                                      on_delete=models.CASCADE, null=True,
                                      help_text="订单号,外键O_ORDERKEY。与L_LINENUMBER联合构成主键",
                                      verbose_name="订单号")
    L_PARTKEY = models.ForeignKey(to="PARTSUPP", to_field="PS_PARTKEY", related_name="LPS_PARTKEY",
                                  on_delete=models.SET_NULL, null=True, verbose_name="零件编号",
                                  help_text="零件编号，外键PS_PARTKEY")
    L_SUPPKEY = models.ForeignKey(to="PARTSUPP", to_field="PS_SUPPKEY", related_name="LPS_SUPPKEY",
                                  on_delete=models.SET_NULL, null=True, verbose_name="供应商编号",
                                  help_text="供应商编号，外键PS_SUPPKEY")
    L_LINENUMBER = models.IntegerField(verbose_name="明细编号", help_text="明细编号 PK")
    L_QUANTITY = models.FloatField(verbose_name="数量", help_text="数量")
    L_EXTENDEDPRICE = models.FloatField(verbose_name="总金额", help_text="总金额", default=0)
    L_DISCOUNT = models.FloatField(verbose_name="折扣", help_text="折扣")
    L_TAX = models.FloatField(verbose_name="税", help_text="税")
    status1 = (
        ('1', "正常交易"),
        ('2', "退货"),
    )
    status2 = (
        ('1', '待支付'),
        ('2', '已支付'),
    )
    L_RETURNFLAG = models.CharField(max_length=1, verbose_name="是否退货", help_text="是否退货", choices=status1,
                                    default=1)  # 选择
    L_LINESTATUS = models.CharField(max_length=1, verbose_name="明细状态", help_text="明细状态", choices=status2,
                                    default=1)  # 选择
    L_SHIPDATE = models.DateField(verbose_name="运输日期", help_text="运输日期,L_SHIPDATE <= L_RECEIPTDAT")  # 限制
    L_COMMITDATE = models.DateField(verbose_name="交付日期", help_text="交付日期")
    L_RECEIPTDATE = models.DateField(verbose_name="收货日期", help_text="收货日期")
    L_SHIPINSTRUCT = models.CharField(max_length=25, verbose_name="运输单位", help_text="运输单位")
    status_3 = (
        ('1', ' 陆运'),
        ('2', ' 海运'),
        ('3', ' 空运'),
    )
    L_SHIPMODE = models.CharField(max_length=1, verbose_name="运输方式", help_text="运输方式", choices=status_3,
                                  default='1')
    L_COMMENT = models.TextField(max_length=44, verbose_name="备注", help_text="备注1")

    class Meta:
        verbose_name = verbose_name_plural = "订单明细"
        unique_together = ("L_ORDERKEY", "L_LINENUMBER")

    def __str__(self):
        return f"{self.L_ORDERKEY},{self.L_LINENUMBER}"

    # def get_absolute_url(self):
    #     return reverse('region-detail', args=[str(self.R_REGIONKEY)])
