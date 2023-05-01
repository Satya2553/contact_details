from .models import *
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import ContactSerailizer
from datetime import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

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



def email(request):
    if request.method == 'POST':
        pdf=request.POST.get('pdf-input')
        path="D:/resumes/myresume3.pdf"
        try:
            email = EmailMessage(
                'subject',
                'Your Paybill is here',
                settings.EMAIL_HOST_USER,
                ['20vv1a0529@gmail.com'],
            )
            email.attach_file(path)
            email.fail_silently = False
            email.send()
            return HttpResponse('Email sent successfully!')
        except Exception as e:
            return HttpResponse('Failed to send email: {}'.format(str(e)), status=500)
    