from urllib.request import Request 
from django.shortcuts import render,HttpResponse 
from Mkart_app.models import Contact
from Mkart_app.models import Login

# Create your views here.
def home(request):
    return render(request,'home.html')

def account(request):
    return render(request,'account.html')

def cart(request):
    return render(request,'cart.html')

def contact(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uphone = request.POST.get('phone')
        uage = request.POST.get('age')
        udetails = Contact(name=uname , phone=uphone,age=uage)
        udetails.save()
        Contact.objects.all()
        # contact.save()
        # Process the data or perform other operations
        return render(request, 'cart.html')
    else:
        return render(request, 'contact.html')


def about(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uphone = request.POST.get('phone')
        uage = request.POST.get('age')
        udetails = Login(name=uname , phone=uphone, age=uage)
        udetails.save()
        Login.objects.all()
        # contact.save()
        # Process the data or perform other operations
        # return render(request, 'cart.html')
        return HttpResponse("Entry sucessfull")
    else:
     return render(request,'about.html')