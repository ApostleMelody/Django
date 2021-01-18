from django.shortcuts import render
from django.http import HttpResponse
from .models import Line
from django.template import loader, Context

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
def csv_download(request):
    response = HttpResponse(content_type='text/csv;charset=gb2312')
    response['Content-Disposition'] = "attachment;filename=result.csv"
    line = Line.objects.filter(name__contains='')
    instant=[['序号','线路名称','设备id','电压等级','线路长度']]
    count = 1
    for i in line:
        instant.append([count,i.name,i.device_id,i.degree,i.length])
        count +=1
    context = {
        'rows': instant
    }
    template = loader.get_template('csv_download.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response

