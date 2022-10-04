from django.urls import reverse
from Authentications.forms import UserForm
from django.views import generic

class RegisterView(generic.CreateView):
    template_name = 'Agents/agent_create.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('login')
