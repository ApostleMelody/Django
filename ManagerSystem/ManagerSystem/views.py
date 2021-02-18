from django.http import HttpResponse
from django.shortcuts import render, redirect ,reverse
def index(request):
    userstatus = request.POST.get('userstatus')
    if userstatus:
        return render(request, 'base.html')
    else:
        return redirect(reverse('UserManager:signin'))


