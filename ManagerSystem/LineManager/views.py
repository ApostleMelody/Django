from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import LineForm
from .models import LineModel
from django.db import connection
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class index(View):
    def get(self, request):
        lines = LineModel.objects.filter(name__icontains='')
        lines_list = []
        for i in lines:
            lines_list.append([i.name, i.length, i.degree])
        context = {'lines': lines_list}
        # print(context['lines'])

        # print(connection.queries)
        return render(request, 'line_index.html', context=context)


    def post(self, request):
        deleteid = request.POST.get('deleteid')
        print(deleteid)
        line = LineModel.objects.get(name=deleteid)
        line.delete()
        messages.info(request, "删除成功")
        return redirect(reverse('LineManager:index'))




class add(View):
    def get(self, request):

        return render(request, 'line_add.html')

    def post(self, request):
        form = LineForm(request.POST)
        if form.is_valid():
            print('表单验证成功')
            name = form.cleaned_data.get('name')
            length = form.cleaned_data.get('length')
            degree = form.cleaned_data.get('degree')
            line = LineModel(name=name, length=length, degree=degree)
            line.save()
            messages.info(request, "添加成功")
        else:
            errors = form.get_errors()
            print(errors)
            for error in errors:
                messages.info(request, error)
        return redirect(reverse('LineManager:add'))