from django.shortcuts import render , redirect
from .models import Contact



def index(request):


    contacts = Contact.objects.all()


    return render(request, 'index.html',{'contacts':contacts})



def add(request):

    if request.method == "POST":
        new_contact = Contact(
            full_name = request.POST['fullname'],
            realation = request.POST['relationship'],
            adress = request.POST['address'],
            email = request.POST.get('e-email', False),
            number = request.POST['phone-number']

        )
        new_contact.save()
        return redirect('contact:index')

    return render(request , 'add.html')


def cotact_profile(request,pk):

    contacts = Contact.objects.get(id=pk)


    return render(request,'contact-profile.html',{'contacts':contacts})