from django.shortcuts import render, redirect
from catalog import models
from catalog.utils.pagination import Pagination  # 自定义的分页组件
from catalog.utils.form import CUSTOMERModelForm


def CUSTOMER_list(request):
    queryset = models.CUSTOMER.objects.all()

    # 分页
    page_object = Pagination(request, queryset)

    return render(request, 'CUSTOMER_list.html', {"queryset": page_object.page_queryset, "page_string": page_object.html()})


def CUSTOMER_add(request):
    title = '添加顾客'
    if request.method == 'GET':
        form = CUSTOMERModelForm
        return render(request, 'change.html', {"form": form, 'title': title})

    # 用户POST提交数据，数据校验
    form = CUSTOMERModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/CUSTOMER/list/')

    # 校验失败，在页面上显示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})


def CUSTOMER_delete(request, nid):
    models.CUSTOMER.objects.filter(C_CUSTKEY=nid).delete()
    return redirect('/CUSTOMER/list/')


def CUSTOMER_edit(request, nid):
    title = '修改顾客'
    # 根据id去数据库获取要编辑的那一行数据（对象）
    row_object = models.CUSTOMER.objects.filter(C_CUSTKEY=nid).first()

    if request.method == 'GET':
        form = CUSTOMERModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, 'title': title})

    form = CUSTOMERModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 校验成功
        form.save()
        return redirect('/CUSTOMER/list/')

    # 校验失败，提示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})
