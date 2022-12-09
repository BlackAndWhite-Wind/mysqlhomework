from django.shortcuts import render, redirect
from catalog import models
from catalog.utils.pagination import Pagination  # 自定义的分页组件
from catalog.utils.form import PARTSUPPModelForm


def PARTSUPP_list(request):
    queryset = models.PARTSUPP.objects.all()

    # 分页
    page_object = Pagination(request, queryset)

    return render(request, 'PARTSUPP_list.html', {"queryset": page_object.page_queryset, "page_string": page_object.html()})


def PARTSUPP_add(request):
    title = '添加零件供应'
    if request.method == 'GET':
        form = PARTSUPPModelForm
        return render(request, 'change.html', {"form": form, 'title': title})

    # 用户POST提交数据，数据校验
    form = PARTSUPPModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/PARTSUPP/list/')

    # 校验失败，在页面上显示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})


def PARTSUPP_delete(request, nid):
    models.PARTSUPP.objects.filter(id=nid).delete()
    return redirect('/PARTSUPP/list/')


def PARTSUPP_edit(request, nid):
    title = '修改零件供应'
    # 根据id去数据库获取要编辑的那一行数据（对象）
    row_object = models.PARTSUPP.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = PARTSUPPModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, 'title': title})

    form = PARTSUPPModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 校验成功
        form.save()
        return redirect('/PARTSUPP/list/')

    # 校验失败，提示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})
