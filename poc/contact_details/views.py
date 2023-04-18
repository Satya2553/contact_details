from .models import *
from .serializers import ContactSerailizer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def contact_list(request):
    if request.method == 'GET':
        contacts = contact_det.objects.all()
        serializer = ContactSerailizer(contacts,many=True)
        return JsonResponse({'contacts':serializer.data})
    
    if request.method == 'POST':
        serializer = ContactSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        
@api_view(['GET','PUT','DELETE'])
def contact_detail(request,id):
    try:
        contact = contact_det.objects.get(pk=id)
    except contact_det.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ContactSerailizer(contact)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ContactSerailizer(contact,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)