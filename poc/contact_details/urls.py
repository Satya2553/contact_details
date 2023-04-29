from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'contact',views.ContactView,basename='contact')

urlpatterns = [
    path('user',views.index),
    path('search',views.index,name='search'),
    path('user_contacts/<str:pk>',views.user_contacts,name='user_contacts'),
] + router.get_urls()