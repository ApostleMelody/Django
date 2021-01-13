from django.shortcuts import render
from django.http import HttpResponse
from .models import Line


def add(request):
    if request.method == 'GET':
        context = {'状态': 'GET方法不允许提交'}
        return render(request,'line_add.html', context=context)
    else:
        name = request.POST.get('name')
        device_id = request.POST.get('device_id')
        degree = request.POST.get('degree')
        length = request.POST.get('length')
        line = Line(name=name, device_id=device_id, degree=degree, length=length)
        line.save()
        context = {'状态':'提交成功'}
        return render(request,'line_add.html', context=context)


def index(request):
    if request.method == 'GET':
        line = Line.objects.filter(name__contains='')
        context = {'line':line}
        return render(request,'line_index.html',context=context)
    else:
        id = request.POST.get('id')
        print(id)
        if id == '':
            name = request.POST.get('name')
            line = Line.objects.filter(name__contains=name)
            context = {'line': line}
            return render(request, 'line_index.html', context=context)
        else:                                                                                          
            line = Line.objects.get(pk=id)
            line.delete()
            line = Line.objects.filter(name__contains='')

            context = { 'state':'删除成功',
                     'line':line}
            return render(request, 'line_index.html', context=context)