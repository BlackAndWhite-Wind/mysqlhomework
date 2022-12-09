from django import forms
from django.core.exceptions import ValidationError  # 错误信息
from catalog import models
from catalog.utils.bootstrap import BootstrapModelForm, BootstrapForm  # 自定义BootstrapModelForm类
from catalog.utils.encode import md5


class LoginForm(BootstrapForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}),
        required=True,  # 验证 必填，默认不能为空
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}, render_value=True),
        required=True
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


class AdminModelForm(BootstrapModelForm):
    """管理员的ModelForm方法"""
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError("两次密码不一致")

        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm


class AdminEditModelForm(BootstrapModelForm):
    """编辑管理员ModelForm"""

    class Meta:
        model = models.Admin
        fields = ['username']


class AdminResetModelForm(BootstrapModelForm):
    """重置管理员密码ModelForm"""
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和新输入的密码是否一致
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError('不能与以前的密码相同')

        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError("密码不一致")

        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm


class REGIONModelForm(BootstrapModelForm):
    """地区的ModelForm方法"""

    class Meta:
        model = models.REGION
        fields = ['R_REGIONKEY', 'R_NAME', 'R_COMMENT', 'PS_SUPPLYCOST', 'PS_COMMENT']


class NATIONModelForm(BootstrapModelForm):
    """国家的ModelForm方法"""

    class Meta:
        model = models.NATION
        fields = ['N_NATIONKEY', 'N_NAME', 'N_REGIONKEY', 'N_COMMENT']


class CUSTOMERModelForm(BootstrapModelForm):
    """顾客的ModelForm方法"""

    class Meta:
        model = models.CUSTOMER
        fields = ['C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT',
                  'C_COMMENT']


class PARTModelForm(BootstrapModelForm):
    """零件的ModelForm方法"""

    class Meta:
        model = models.PART
        fields = ['P_PARTKEY', 'P_NAME', 'P_MFGR', 'P_BRAND', 'P_TYPE', 'P_SIZE', 'P_CONTAINER', 'P_RETAILPRICE',
                  'P_COMMENT']


class SUPPLIERModelForm(BootstrapModelForm):
    """供应商的ModelForm方法"""

    class Meta:
        model = models.SUPPLIER
        fields = ['S_SUPPKEY', 'S_NAME', 'S_ADDRESS', 'S_NATIONKEY', 'S_PHONE', 'S_ACCTBAL', 'S_COMMENT']


class PARTSUPPModelForm(BootstrapModelForm):
    """零件供应的ModelForm方法"""

    class Meta:
        model = models.PARTSUPP
        fields = ['PS_PARTKEY', 'PS_SUPPKEY', 'PS_AVAILQTY', 'PS_SUPPLYCOST', 'PS_COMMENT']


class ORDERSModelForm(BootstrapModelForm):
    """订单的ModelForm方法"""

    class Meta:
        model = models.ORDERS
        fields = ['O_ORDERKEY', 'O_CUSTKEY', 'O_ORDERSTATUS', 'O_TOTALPRICE', 'O_ORDERDATE', 'O_ORDERPRIORITY',
                  'O_CLERK', 'O_SHIPPRIORITY', 'O_COMMENT']


class LINEITEMModelForm(BootstrapModelForm):
    """订单的ModelForm方法"""

    class Meta:
        model = models.LINEITEM
        fields = ['L_ORDERKEY', 'L_PARTKEY', 'L_SUPPKEY', 'L_LINENUMBER', 'L_QUANTITY', 'L_EXTENDEDPRICE', 'L_DISCOUNT',
                  'L_TAX', 'L_RETURNFLAG', 'L_LINESTATUS', 'L_SHIPDATE', 'L_COMMITDATE', 'L_RECEIPTDATE',
                  'L_SHIPINSTRUCT', 'L_SHIPMODE', 'L_COMMENT']
