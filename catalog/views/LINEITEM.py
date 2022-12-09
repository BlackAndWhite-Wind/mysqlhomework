from django.shortcuts import render, redirect
from catalog import models
from catalog.utils.pagination import Pagination  # 自定义的分页组件
from catalog.utils.form import LINEITEMModelForm
from django.contrib import messages 


def LINEITEM_list(request,nid):
    queryset = models.LINEITEM.objects.filter(id=nid)

    # 分页
    page_object = Pagination(request, queryset)

    return render(request, 'LINEITEM_list.html', {"queryset": page_object.page_queryset, "page_string": page_object.html()})


def LINEITEM_add(request):
    title = '添加订单明细'
    if request.method == 'GET':
        form = LINEITEMModelForm
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})


    form = LINEITEMModelForm(data=request.POST) 

    if request.POST['L_SHIPDATE'] > request.POST['L_COMMITDATE']  or   request.POST['L_COMMITDATE'] > request.POST['L_RECEIPTDATE']:
        messages.warning(request, "错误，需要满足条件,时间：运输小于交付小于收货")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})

    if models.PARTSUPP.objects.filter(PS_PARTKEY=request.POST['L_PARTKEY']).values()[0].get('id') != models.PARTSUPP.objects.filter(PS_SUPPKEY=request.POST['L_SUPPKEY']).values()[0].get('id'):
        messages.warning(request, "错误，零件编号与供应商编号未对应")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})

    if models.PARTSUPP.objects.filter(PS_PARTKEY=request.POST['L_PARTKEY']).values()[0].get('PS_AVAILQTY') < float(request.POST['L_QUANTITY']):
        messages.warning(request, "错误，数量大于供应最大值")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})     

    if float(request.POST['L_DISCOUNT']) >=1 or float(request.POST['L_DISCOUNT']) <=0:
        messages.warning(request, "错误, 折扣应在0到1之间")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})    

    if float(request.POST['L_TAX']) >=1 or float(request.POST['L_TAX']) <=0:
        messages.warning(request, "错误, 税应该在0到1之间")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})      

    if float(request.POST['L_EXTENDEDPRICE']) !=  float(request.POST['L_QUANTITY']) * models.PARTSUPP.objects.filter(PS_PARTKEY=request.POST['L_PARTKEY']).values()[0].get('PS_SUPPLYCOST') * (1-float(request.POST['L_DISCOUNT'])) * (1+float(request.POST['L_TAX'])):
        return _extracted_from_LINEITEM_add_31(request, form, title)
    # 用户POST提交数据，数据校验
    if form.is_valid():
    # 如果数据合法，保存到数据库
        models.ORDERS.objects.filter(O_ORDERKEY=request.POST['L_ORDERKEY']).update(O_TOTALPRICE=float(request.POST['L_EXTENDEDPRICE']))
        form.save()
        return redirect('/ORDERS/list/')


# TODO Rename this here and in `LINEITEM_add`
def _extracted_from_LINEITEM_add_31(request, form, title):
    messages.warning(request, "错误，总价钱不对")
    data=request.POST
    _mutable = data._mutable
    data._mutable = True
    data['L_EXTENDEDPRICE']=float(request.POST['L_QUANTITY']) * models.PARTSUPP.objects.filter(PS_PARTKEY=request.POST['L_PARTKEY']).values()[0].get('PS_SUPPLYCOST') * (1-float(request.POST['L_DISCOUNT'])) * (1+float(request.POST['L_TAX']))
    data._mutable = _mutable
    return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})

    


def LINEITEM_delete(request, nid):
    models.LINEITEM.objects.filter(id=nid).delete()
    return redirect('/ORDERS/list/')


def LINEITEM_edit(request, nid):
    title = '修改订单明细'
    row_object = models.LINEITEM.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = LINEITEMModelForm(instance=row_object)
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})

    form = LINEITEMModelForm(data=request.POST,instance=row_object) 

    if request.POST['L_SHIPDATE'] > request.POST['L_COMMITDATE']  or   request.POST['L_COMMITDATE'] > request.POST['L_RECEIPTDATE']:
        messages.warning(request, "错误，需要满足条件,时间：运输小于交付小于收货")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})

    if models.PARTSUPP.objects.filter(PS_PARTKEY=request.POST['L_PARTKEY']).values()[0].get('id') != models.PARTSUPP.objects.filter(PS_SUPPKEY=request.POST['L_SUPPKEY']).values()[0].get('id'):
        messages.warning(request, "错误，零件编号与供应商编号未对应")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})

    if models.PARTSUPP.objects.filter(PS_PARTKEY=request.POST['L_PARTKEY']).values()[0].get('PS_AVAILQTY') < float(request.POST['L_QUANTITY']):
        messages.warning(request, "错误，数量大于供应最大值")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})     

    if float(request.POST['L_DISCOUNT']) >=1 or float(request.POST['L_DISCOUNT']) <=0:
        messages.warning(request, "错误，折扣应在0到1之间")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})    

    if float(request.POST['L_TAX']) >=1 or float(request.POST['L_TAX']) <=0:
        messages.warning(request, "错误，税应该在0到1之间")
        return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})    

    if float(request.POST['L_EXTENDEDPRICE']) !=  float(request.POST['L_QUANTITY']) * models.PARTSUPP.objects.filter(PS_PARTKEY=request.POST['L_PARTKEY']).values()[0].get('PS_SUPPLYCOST') * (1-float(request.POST['L_DISCOUNT'])) * (1+float(request.POST['L_TAX'])):
        return _extracted_from_LINEITEM_edit_31(request, form, title)
    # 用户POST提交数据，数据校验
    if form.is_valid():
    # 如果数据合法，保存到数据库
        models.ORDERS.objects.filter(O_ORDERKEY=request.POST['L_ORDERKEY']).update(O_TOTALPRICE=float(request.POST['L_EXTENDEDPRICE']))
        form.save()
        return redirect('/ORDERS/list/')


# TODO Rename this here and in `LINEITEM_edit`
def _extracted_from_LINEITEM_edit_31(request, form, title):
    messages.warning(request, "错误，总价钱不对")
    data=request.POST
    _mutable = data._mutable
    data._mutable = True
    data['L_EXTENDEDPRICE']=float(request.POST['L_QUANTITY']) * models.PARTSUPP.objects.filter(PS_PARTKEY=request.POST['L_PARTKEY']).values()[0].get('PS_SUPPLYCOST') * (1-float(request.POST['L_DISCOUNT'])) * (1+float(request.POST['L_TAX']))
    data._mutable = _mutable
    return render(request, 'LINEITEM_change.html', {"form": form, 'title': title})
