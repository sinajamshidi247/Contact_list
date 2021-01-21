from django.shortcuts import render , redirect
from .models import Contact



def index(request):


    contacts = Contact.objects.all()

    search_input = request.GET.get('search_area')
    if search_input :
        contacts = Contact.objects.filter(full_name_icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''


    return render(request, 'index.html',{'contacts':contacts,'search_input':search_input})



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

def edit(request,pk):
    contacts = Contact.objects.get(id=pk)
    if request.method == "POST":
        
        contacts.full_name = request.POST['fullname']
        contacts.realation = request.POST['relationship']
        contacts.adress = request.POST['address']
        contacts.email = request.POST.get('e-email', False)
        contacts.number = request.POST['phone-number']
        contacts.save()
        return redirect('contact:index')


    return render(request,'edit.html',{'contacts':contacts})



def delete(request,pk):
    contacts = Contact.objects.get(id=pk)

    if request.method == "POST":
        contacts.delete()
        return redirect('contact:index')
    return render(request,'delete.html',{'contacts':contacts})