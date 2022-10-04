from django import forms
from Leads.models import Lead,Agent

class CreateLead(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name','last_name','age','email','description','address','occupation','phone_number','category','agent']


class AssignLeadToAgent(forms.Form):
    agent = forms.ModelChoiceField(queryset = Agent.objects.none())

    def __init__(self,*args,**kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(orgarnization =request.user.userprofile)
        super(AssignLeadToAgent,self).__init__(*args,**kwargs)
        self.fields['agent'].queryset = agents