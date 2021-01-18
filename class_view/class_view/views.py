from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse


class Class_View(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("类视图")

class Class_View2(View):
    def get(self, request, *args, **kwargs):
        return render(request,'add_book.html')
    def post(self, request, *args, **kwargs):
        book_name = request.POST.get('name')
        print(book_name)
        return HttpResponse('Success')