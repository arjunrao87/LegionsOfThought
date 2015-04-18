from django.db import models

# Create your models here.


class ContactUs( models.Model ):
    name = models.CharField( max_length=100 )
    email = models.CharField( max_length=100 )
    phone = models.CharField( max_length=100 )
    message = models.CharField( max_length=250 )
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name