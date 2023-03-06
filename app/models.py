from django.db import models    
from datetime import date
import datetime
from django.db.models.base import Model
from usuarios.models import Usuario

class Controle(models.Model):    
    num_lic = models.CharField(max_length = 20, blank = False)
    num_sap = models.CharField(max_length = 15, blank = False)
    objeto = models.CharField(max_length = 300, blank = False)
    
    class Meta:
            verbose_name = 'Controle TES'

    def __str__(self):
        return self.num_lic

