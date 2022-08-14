from django.db import models
from django.urls import reverse

# Create your models here.
class Marks(models.Model):
    gfc = models.IntegerField()
    eng = models.IntegerField()
    wt1 = models.IntegerField()
    bmee = models.IntegerField()
    ampp = models.IntegerField()

    def get_absolute_url(self):
         return reverse('listmarks')
   
        
