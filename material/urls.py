"""material URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path


from django.urls import path
from django.views.static import serve
from django.conf import settings
# from catalog.views import depart, user, pretty, admin, account, city, avatar, task, order, chart
from catalog.views import  account,admin,REGION,NATION,CUSTOMER,PART,SUPPLIER,PARTSUPP,ORDERS,LINEITEM

urlpatterns = [
    path('', account.login),
    
    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),
    
    # 注册
    path('register/', account.register),
    
    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),
    
    # 地区管理
    path('REGION/list/', REGION.REGION_list),
    path('REGION/add/', REGION.REGION_add),
    path('REGION/<int:nid>/delete/', REGION.REGION_delete),
    path('REGION/<int:nid>/edit/', REGION.REGION_edit),
    
    # 国家管理
    path('NATION/list/', NATION.NATION_list),
    path('NATION/add/', NATION.NATION_add),
    path('NATION/<int:nid>/delete/', NATION.NATION_delete),
    path('NATION/<int:nid>/edit/', NATION.NATION_edit),
    
    # 顾客管理
    path('CUSTOMER/list/', CUSTOMER.CUSTOMER_list),
    path('CUSTOMER/add/', CUSTOMER.CUSTOMER_add),
    path('CUSTOMER/<int:nid>/delete/', CUSTOMER.CUSTOMER_delete),
    path('CUSTOMER/<int:nid>/edit/', CUSTOMER.CUSTOMER_edit),
    
    # 零件管理
    path('PART/list/', PART.PART_list),
    path('PART/add/', PART.PART_add),
    path('PART/<int:nid>/delete/', PART.PART_delete),
    path('PART/<int:nid>/edit/', PART.PART_edit),
    
    
    # 供应商管理
    path('SUPPLIER/list/', SUPPLIER.SUPPLIER_list),
    path('SUPPLIER/add/', SUPPLIER.SUPPLIER_add),
    path('SUPPLIER/<int:nid>/delete/', SUPPLIER.SUPPLIER_delete),
    path('SUPPLIER/<int:nid>/edit/', SUPPLIER.SUPPLIER_edit),
    
    # 零件供应管理
    path('PARTSUPP/list/', PARTSUPP.PARTSUPP_list),
    path('PARTSUPP/add/', PARTSUPP.PARTSUPP_add),
    path('PARTSUPP/<int:nid>/delete/', PARTSUPP.PARTSUPP_delete),
    path('PARTSUPP/<int:nid>/edit/', PARTSUPP.PARTSUPP_edit),    
    
    # 订单管理
    path('ORDERS/list/', ORDERS.ORDERS_list),
    path('ORDERS/add/', ORDERS.ORDERS_add),
    path('ORDERS/<int:nid>/delete/', ORDERS.ORDERS_delete),
    path('ORDERS/<int:nid>/edit/', ORDERS.ORDERS_edit),    
    
    # 订单明细管理
    path('LINEITEM/<int:nid>/list/', LINEITEM.LINEITEM_list),
    path('LINEITEM/add/', LINEITEM.LINEITEM_add),
    path('LINEITEM/<int:nid>/delete/', LINEITEM.LINEITEM_delete),
    path('LINEITEM/<int:nid>/edit/', LINEITEM.LINEITEM_edit),    
]
