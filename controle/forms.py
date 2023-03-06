from django.forms import ModelForm
from controle.models import Controle

class controleForm(ModelForm): 
    class Meta: 
        model = Controle
        fields = ['num_lic','num_sap','objeto ']      
                                  
                       