from django import forms
from .models import DataSheet
"""formularios para 
la parte admin de django"""


class DataSheetForm(forms.ModelForm):
    class Meta:
        model = DataSheet
        fields = [
            'asin',
            'titulo',
            'bullet_1',
            'bullet_2',
            'bullet_3',
            'bullet_4',
            'bullet_5',
        ]

