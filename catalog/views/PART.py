from django.shortcuts import render, redirect
from catalog import models
from catalog.utils.pagination import Pagination  # 自定义的分页组件
from catalog.utils.form import PARTModelForm


def PART_list(request):
    queryset = models.PART.objects.all()

    # 分页
    page_object = Pagination(request, queryset)

    return render(request, 'PART_list.html', {"queryset": page_object.page_queryset, "page_string": page_object.html()})


def PART_add(request):
    title = '添加零件'
    if request.method == 'GET':
        form = PARTModelForm
        return render(request, 'change.html', {"form": form, 'title': title})

    # 用户POST提交数据，数据校验
    form = PARTModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/PART/list/')

    # 校验失败，在页面上显示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})


def PART_delete(request, nid):
    models.PART.objects.filter(P_PARTKEY=nid).delete()
    return redirect('/PART/list/')


def PART_edit(request, nid):
    title = '修改零件'
    # 根据id去数据库获取要编辑的那一行数据（对象）
    row_object = models.PART.objects.filter(P_PARTKEY=nid).first()

    if request.method == 'GET':
        form = PARTModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, 'title': title})

    form = PARTModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 校验成功
        form.save()
        return redirect('/PART/list/')

    # 校验失败，提示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})
