from django.db import models
  
class Contact (models.model):
    frist_name=models.CharField(max_length=10,)
    last_name=models.CharField(max_length=10,)
    phone_number=models.IntegerField(max_length=16 )
    e_mail=models.EmailField


    
