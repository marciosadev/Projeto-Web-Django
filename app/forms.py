from django.forms import ModelForm
from app.models import Controle

class ControleForm(ModelForm):
    class Meta:
        model = Controle
        fields = ['num_lic', 'num_sap', 'objeto']        
   