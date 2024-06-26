from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return self.full_name