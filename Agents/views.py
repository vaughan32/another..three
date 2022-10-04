from django.urls import reverse
from Leads.models import Agent
from django.views import generic
from Agents.forms import CreateAgent
from Agents.mixins import OrgarnizerCheckLoginRequiredMixin
from django.core.mail import send_mail
import random

class AgentList(OrgarnizerCheckLoginRequiredMixin,generic.ListView):
    context_object_name = 'all_agents'
    template_name = 'Agents/agent_list.html'

    def get_queryset(self):
        orgarnization = self.request.user.userprofile
        return Agent.objects.filter(orgarnization = orgarnization)


class AgentCreate(OrgarnizerCheckLoginRequiredMixin,generic.CreateView):
    template_name = 'Agents/agent_create.html'
    form_class = CreateAgent

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_orgarnizer = False
        user.is_agent = True
        user.set_password(f'{random.randint(0,10000000)}')
        user.save()
        Agent.objects.create( user= user,orgarnization=self.request.user.userprofile)
        send_mail(
            subject='You are Invited To Be An Agent',
            message='You were added as an agent on this app.kindly change your password,Login and start tasking with your leads.',
            from_email='TheadminOfTheApp@gmail.com',
            recipient_list=[user.email])
        return super(AgentCreate,self).form_valid(form)

    def get_success_url(self):
        return reverse('agent_list')


class AgentDetail(OrgarnizerCheckLoginRequiredMixin,generic.DetailView):
    context_object_name = 'agent_detail'
    template_name = 'Agents/agent_detail.html'

    def get_queryset(self):
        orgarnization = self.request.user.userprofile
        return Agent.objects.filter(orgarnization = orgarnization)


class AgentUpdate(OrgarnizerCheckLoginRequiredMixin,generic.UpdateView):
    context_object_name = 'agent_detail'
    template_name = 'Agents/agent_update.html'
    form_class = CreateAgent

    def get_queryset(self):
        orgarnization = self.request.user.userprofile
        return Agent.objects.filter(orgarnization = orgarnization)

    def get_success_url(self):
        return reverse('lead_list')


class AgentDelete(OrgarnizerCheckLoginRequiredMixin,generic.DeleteView):
    template_name = 'Agents/agent_delete.html'
    context_object_name = 'agent_detail'

    def get_queryset(self):
        orgarnization = self.request.user.userprofile
        return Agent.objects.filter(orgarnization = orgarnization)

    def get_success_url(self):
        return reverse('agent_list')