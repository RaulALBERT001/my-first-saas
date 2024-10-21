from django.db import models

# Create your models here.
class PageVisitis(models.Model):  
    # id already exists by default, and with auto increment on it 
    path = models.TextField(blank = True,  null = True)
    timestamp = models.DateTimeField(auto_now_add=True)