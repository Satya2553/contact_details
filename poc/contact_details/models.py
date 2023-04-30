from django.db import models

# Create your models here.


class contact_det(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    company = models.CharField(max_length=20)
    job_title = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    birthday = models.DateField()
    notes = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " +self.last_name
    
    
class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    contacts = models.ManyToManyField(contact_det)

    def __str__(self):
        return self.username
    
class Payment(models.Model):
    contact = models.OneToOneField(contact_det, on_delete=models.CASCADE)
    payable_amount = models.DecimalField(max_digits=8, decimal_places=2)
    days_attended = models.IntegerField()
    total_days = models.IntegerField()

    def __str__(self):
         return f"{self.contact.first_name} {self.contact.last_name} Payment"