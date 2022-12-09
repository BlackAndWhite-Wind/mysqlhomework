from django.shortcuts import render, redirect
from catalog import models
from catalog.utils.pagination import Pagination  # 自定义的分页组件
from catalog.utils.form import REGIONModelForm


def REGION_list(request):
    queryset = models.REGION.objects.all()

    # 分页
    page_object = Pagination(request, queryset)

    return render(request, 'REGION_list.html', {"queryset": page_object.page_queryset, "page_string": page_object.html()})


def REGION_add(request):
    title = '添加地区'
    if request.method == 'GET':
        form = REGIONModelForm
        return render(request, 'change.html', {"form": form, 'title': title})

    # 用户POST提交数据，数据校验
    form = REGIONModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/REGION/list/')

    # 校验失败，在页面上显示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})


def REGION_delete(request, nid):
    models.REGION.objects.filter(R_REGIONKEY=nid).delete()
    return redirect('/REGION/list/')


def REGION_edit(request, nid):
    """修改部门"""
    title = '修改部门'
    # 根据id去数据库获取要编辑的那一行数据（对象）
    row_object = models.REGION.objects.filter(R_REGIONKEY=nid).first()

    if request.method == 'GET':
        form = REGIONModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, 'title': title})

    form = REGIONModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 校验成功
        form.save()
        return redirect('/REGION/list/')

    # 校验失败，提示错误信息
    return render(request, 'change.html', {"form": form, 'title': title})
