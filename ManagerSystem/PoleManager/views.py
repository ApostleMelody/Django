from django.shortcuts import render
from django.views.generic import View
from LineManager.models import LineModel
from django.http import HttpResponse
class index(View):
    def get(self, request):
        lines = LineModel.objects.filter(name__icontains='')
        lines_list = []
        for i in lines:
            lines_list.append([i.name, i.length, i.degree])
        context = {'lines': lines_list}
        # print(context['lines'])

        # print(connection.queries)
        return render(request, 'pole_index.html', context=context)

    def post(self, request):
        return HttpResponse('暂时无内容')