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