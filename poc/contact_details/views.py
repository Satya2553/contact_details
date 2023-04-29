from .models import *
from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet
from .serializers import ContactSerailizer

class ContactView(ModelViewSet):
    queryset = contact_det.objects.all()
    serializer_class = ContactSerailizer

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        return redirect('user_contacts/'+ username)
    return render(request,'index.html')

def user_contacts(request, pk):
    try:
        user = User.objects.get(username=pk)
        user_contacts = user.contacts.all()
    except User.DoesNotExist:
        user_contacts = None

    context = {
        'user_contacts': user_contacts
    }
    return render(request, 'contact.html', context)