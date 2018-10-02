from django import forms
from .models import ReceiverModel

class ReceiveForm(forms.ModelForm):
    class Meta:
        model = ReceiverModel
        fields = ('file_received', )


