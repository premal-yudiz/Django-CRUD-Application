from django.shortcuts import render,redirect
from .forms import Student_registration
from django.http import HttpResponse
from .models import User
# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm = Student_registration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Student_registration()
        else:
            return HttpResponse("hey")

    else:
        fm = Student_registration()
    std = User.objects.all()
    return render(request,'addandshow.html',{'form':fm, 'std':std})


def delete(request,id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        user.delete()
        return redirect('/')
    
def update(request,id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        fm = Student_registration(request.POST,instance=user)
        if fm.is_valid():
            fm.save()
            return redirect('/')


    else:
        user = User.objects.get(pk=id)
        fm = Student_registration(instance = user)

    return render(request,'update.html',{"form":fm})