from django.urls import path, include
from . import views
urlpatterns = [
    path('contacts',views.contact_list,name='contacts'),
    path('contacts/<int:id>',views.contact_detail)
]