from django.forms import ModelForm
from .models import Dreamboard

class DreamboardForm(ModelForm):
    class Meta:
        model = Dreamboard
        fields = '__all__'