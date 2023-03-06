from django.db import models    
from datetime import date
import datetime
from django.db.models.base import Model
from usuarios.models import Usuario

class Controle(models.Model):
    
    ELETR_CHOICES = (
        ("S", "Sim"),
        ("N", "Não"),
        
    )
    
    MOD_CHOICES = (
        ("LI", "Licitação Sabesp"),
        ("PG", "Pregão"),
        ("DV", "Dispensa"),
        ("CV", "Convite"),
        
    )  
    
    JULG_CHOICES = (
        ("MP", "Menor preço"),
        ("TP", "Técnica e Preço"),
        
    )    
    
    DISP_CHOICES = (
        ("A", "Aberta"),
        ("F", "Fechada"),
        
    ) 
    
    num_lic = models.CharField(max_length = 20, blank = False)
    num_sap = models.CharField(max_length = 15, blank = False)
    objeto = models.CharField(max_length = 300, blank = False)
    historico = models.CharField(max_length = 300, blank = True) 
    resp_pac = models.CharField(max_length = 30, blank = False)
    an_lic = models.CharField(max_length = 30, blank = False)
    area_req = models.CharField(max_length = 10, blank = False) 
    crit_julg = models.CharField(max_length=2, choices=JULG_CHOICES, blank=False, null=False)
    mod_contr = models.CharField(max_length=2, choices=MOD_CHOICES, blank=False, null=False) 
    proc_ele = models.CharField(max_length=1, choices=ELETR_CHOICES, blank=False, null=False)
    data_i0 = models.DateField()
    disputa = models.CharField(max_length=1, choices=DISP_CHOICES, blank=False, null=False)
    fonte_rec = models.CharField(max_length = 20, blank = False)
    orcado = models.CharField(max_length = 25, blank = False)
    valor_contr = models.CharField(max_length = 25, blank = True)
    vencedora = models.CharField(max_length = 25, blank = True)
    comissao = models.CharField(max_length = 300, blank = True) 
    
    class Meta:
        verbose_name = 'Controle TES'

    def __str__(self):
        return self.num_lic

