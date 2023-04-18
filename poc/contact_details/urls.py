from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('contacts',views.contact_list,name='contacts'),
    path('contacts/<int:id>',views.contact_detail),
    path('search',views.index,name='search'),
    path('user_contacts/<str:pk>',views.user_contacts,name='user_contacts')
    
]