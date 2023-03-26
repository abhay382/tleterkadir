from django.shortcuts import render
from.models import Contact
# Create your views here.

def index(request):
    return render (request,'index.html')


def About(request):
    return render (request,'About.html')

def contact (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})



def Gallery(request):
    return render (request,'Gallery.html')


def Leatherj(request):
    return render (request,'Leather-journal-manufacturer.html')


def Leatherej(request):
    return render (request,'embossed-leather-manufacturer.html')

def Leatherevj(request):
    return render (request,'Vintage-leather-journal.html')


def Leatherdufflebag(request):
    return render (request,'Leather-Duffle-Bags-manufacturer.html')

def Leatherbackpack(request):
    return render (request,'Leather-Backpacks-manufacturer.html')

def Leatherslingbag(request):
    return render (request,'Leather-Sling-Bags-manufacturer.html')

def Leathertotebag(request):
    return render (request,'Leather-Tote-Bags-manufacturer.html')


def Leathermessangerbag(request):
    return render (request,'Leather-Messenger-Bags-manufacturer.html')

def Leatherlaptopbag(request):
    return render (request,'Leather-Laptop-Bags-manufacturer.html')

def Leatherbriefcase(request):
    return render (request,'Leather-Briefcase-&-Bags.html')

def Leatherwashbag(request):
    return render (request,'Leather-Wash-Bags-Toiletry-Bags.html')

def Leathersaddlebag(request):
    return render (request,'Leather-Saddle-Bags-manufacturer.html')

def hobo(request):
    return render (request,'Leather-Hobo-Bags.html')


def Lb(request):
    return render (request,'Leather-bag-manufacturer.html')