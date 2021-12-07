
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rent.models import Rent
from rent.form import form_class
def index (request):
    if request.method=="POST":
        name=(request.POST['name'])
        house_name=(request.POST['hname'])
        house_no=(request.POST['hno'])
        rent=(request.POST['rno'])
        re=Rent()
        re.name=name
        re.house_name=house_name
        re.house_no=house_no
        re.rent=rent
        re.save()
        return redirect("index")

    return render(request,'index.html')
def rent(request):
    rent=Rent.objects.all()
    context={'rent':rent}
    return  render(request,'rent.html',context)
def form(request):
    form=form_class()
    context={'form':form}
    return render(request,'form.html',context)

# Create your views here.
