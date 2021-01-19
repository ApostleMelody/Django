from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        return render(request,'index.html')
