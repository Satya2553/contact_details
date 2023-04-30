from .models import *
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import ContactSerailizer
from datetime import datetime

class ContactView(ModelViewSet):
    queryset = contact_det.objects.all()
    serializer_class = ContactSerailizer

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        return redirect('user_contacts', pk=username)
    all_contacts = contact_det.objects.all()
    context = {
        'all_contacts': all_contacts
    }
    return render(request, 'index.html', context)


def user_contacts(request, pk):
    try:
        user = User.objects.get(username=pk)
        user_contacts = user.contacts.all()
    except User.DoesNotExist:
        user_contacts = None
    context = {
        'user_contacts': user_contacts,
    }
    return render(request, 'contact.html', context)

def contact_payable(request, contact_id):
    contact = get_object_or_404(contact_det, id=contact_id)
    payment = Payment.objects.get(contact=contact)
    context = {
        'contact': contact,
        'payment': payment,
        'date': datetime.today()
    }
    return render(request, 'paybill.html', context)
    
