from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class StaffActivityFilterForm(forms.Form):
    ROLE_CHOICES=[
        ("caregiver","Caregiver"),
        ("alternate","Alternate"),
        ("rn","RN"),
    ]

    STATUS_CHOICES=[
        ("active","Active"),
        ("inactive","Inactive")
    ]

    role=forms.ChoiceField(choices=ROLE_CHOICES,required=False)
    status=forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    start_date=forms.DateField(required=False, widget=forms.DateInput(attrs={"type":"date"}))
    end_date=forms.DateField(required=False, widget=forms.DateInput(attrs={"type":"date"}))

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method="get"
        self.helper.add_input(Submit("filter","Apply Filters"))