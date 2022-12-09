from django.shortcuts import render, redirect
from catalog import models
from catalog.utils.pagination import Pagination  # 自定义的分页组件
from catalog.utils.form import ORDERSModelForm
from django.contrib import messages 


def ORDERS_list(request):
    queryset = models.ORDERS.objects.all()
    for obj in queryset:
        obj.O_ORDERSTATUS=obj.get_O_ORDERSTATUS_display()
        obj.O_ORDERPRIORITY=obj.get_O_ORDERPRIORITY_display()
        obj.O_SHIPPRIORITY=obj.get_O_SHIPPRIORITY_display()  
        obj.lineitem_isnot = models.LINEITEM.objects.filter(L_ORDERKEY=obj.O_ORDERKEY).count()
        if obj.lineitem_isnot==1:
            obj.lineitem_id = int(models.LINEITEM.objects.filter(L_ORDERKEY=obj.O_ORDERKEY).values()[0].get('id'))
        
    # 分页
    page_object = Pagination(request, queryset)

    return render(request, 'ORDERS_list.html', {"queryset": page_object.page_queryset, "page_string": page_object.html()})


def ORDERS_add(request):
    title = '添加订单'
    if request.method == 'GET':
        form = ORDERSModelForm
        return render(request, 'ORDERS_change.html', {"form": form, 'title': title})

    if request.POST['O_TOTALPRICE']!=0:
        data = _extracted_from_ORDERS_add_8(request)
    form = ORDERSModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        messages.warning(request, "请建立订单明细")
        return redirect('/ORDERS/list/')

    # 校验失败，在页面上显示错误信息
    return render(request, 'ORDERS_change.html', {"form": form, 'title': title})


# TODO Rename this here and in `ORDERS_add`
def _extracted_from_ORDERS_add_8(request):
    messages.warning(request, "订单金额请到订单明细进行添加，默认0.0")
    result = request.POST
    _mutable = result._mutable
    result._mutable = True
    result['O_TOTALPRICE'] = 0.0
    result._mutable = _mutable
    return result


def ORDERS_delete(request, nid):
    models.ORDERS.objects.filter(O_ORDERKEY=nid).delete()
    return redirect('/ORDERS/list/')


def ORDERS_edit(request, nid):
    title = '修改订单'
    # 根据id去数据库获取要编辑的那一行数据（对象）
    row_object = models.ORDERS.objects.filter(O_ORDERKEY=nid).first()
    if request.method == 'GET':
        form = ORDERSModelForm(instance=row_object)
        return render(request, 'ORDERS_change.html', {"form": form, 'title': title})
    if float(request.POST['O_TOTALPRICE'])!=float(models.ORDERS.objects.filter(O_ORDERKEY=nid).values()[0].get('O_TOTALPRICE')):
        return _extracted_from_ORDERS_edit_9(request, nid, row_object, title)
    form = ORDERSModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 校验成功
        form.save()
        return redirect('/ORDERS/list/')

    # 校验失败，提示错误信息
    return render(request, 'ORDERS_change.html', {"form": form, 'title': title})


# TODO Rename this here and in `ORDERS_edit`
def _extracted_from_ORDERS_edit_9(request, nid, row_object, title):
    messages.warning(request, "订单金额请到订单明细进行修改")
    data=request.POST
    _mutable = data._mutable
    data._mutable = True
    data['O_TOTALPRICE']=models.ORDERS.objects.filter(O_ORDERKEY=nid).values()[0].get('O_TOTALPRICE')
    data._mutable = _mutable
    form = ORDERSModelForm(data=request.POST, instance=row_object)
    return render(request, 'ORDERS_change.html', {"form": form, 'title': title})
