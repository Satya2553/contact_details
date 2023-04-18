from rest_framework import serializers
from .models import *
class ContactSerailizer(serializers.ModelSerializer):
    class Meta:
        model = contact_det
        fields = ['id','first_name','last_name','company','job_title','email','phone','birthday','notes']