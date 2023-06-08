from django import forms

from .models import Objective


class ObjectiveForm(forms.ModelForm):

    class Meta:
        model = Objective
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "objective": forms.TextInput(attrs={"class": "form-control"}),
            "value": forms.Select(attrs={"class": "form-select"}),
        }
