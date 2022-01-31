from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    cmp_nm = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
