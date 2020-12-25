from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    context = {'value':'张三',
               'mytime':datetime(year=2020,month=12,day=18,hour=18,
                                minute=0,second=0)}
    return render(request, 'index.html',context=context)