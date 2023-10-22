from django import forms
from django.forms.widgets import Select


class SelectOutputTypeForm(forms.Form):
    CHOISES = (("charts", "Charts"), ("table", "Table"))
    choise = forms.ChoiceField(choices=CHOISES, widget=Select)
