from django import forms

from .models import abs_immigration
#
# class abs_immigration_form(forms.ModelForm):
#
#     class Meta:
#         model= abs_immigration
#         fields=[
#             'title'
#         ]

class RawImmigrationForm(forms.Form):
    migration_type = forms.ChoiceField(choices=[(1,"Arriving"),(2,"Departing"),(3,"Net Migration")])
    gender = forms.ChoiceField(choices=[("Males","Males"),("Females","Females"),("Persons","Persons")])
    region= forms.ChoiceField(choices=[("Australia","Australia"),("Victoria","Victoria")])

