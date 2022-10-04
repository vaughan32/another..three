from django import forms
from Leads.models import Lead,Category

class CategoryLead(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['category']

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']