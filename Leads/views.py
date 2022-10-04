from django.urls import reverse
from Leads.models import Lead
from Leads.forms import CreateLead,AssignLeadToAgent
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from Agents.mixins import OrgarnizerCheckLoginRequiredMixin

class LandingPage(generic.TemplateView):
    template_name = 'Leads/landing_page.html'


class LeadList(LoginRequiredMixin,generic.ListView):
    context_object_name = 'all_leads'
    template_name = 'Leads/lead_list.html'

# Filtering the leads to the current profile and agent
    def get_queryset(self):
        user = self.request.user
        # Filtering the leads to the current profile
        if user.is_orgarnizer:
            queryset = Lead.objects.filter(orgarnization = user.userprofile,agent__isnull=False)
        else:
            # Filtering the leads to the current agent orgarnization
            queryset = Lead.objects.filter(orgarnization = user.agent.orgarnization,agent__isnull=False)
            # Filtering the leads to the current agent
            queryset = queryset.filter(agent__user = user)
        return queryset

# filtering the assigned and unassigned leads
    def get_context_data(self, **kwargs):
        context = super(LeadList,self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_orgarnizer:
            queryset = Lead.objects.filter(orgarnization = user.userprofile,agent__isnull=True)
            context.update({'unassigned_leads' : queryset})
        return context


class LeadDetails(LoginRequiredMixin,generic.DetailView):
    context_object_name = 'lead_detail'
    template_name = 'Leads/lead_detail.html'

# Filtering the leads to the current profile and agent
    def get_queryset(self):
        user = self.request.user
        # Filtering the leads to the current profile
        if user.is_orgarnizer:
            queryset = Lead.objects.filter(orgarnization = user.userprofile)
        else:
            # Filtering the leads to the current agent orgarnization
            queryset = Lead.objects.filter(orgarnization = user.agent.orgarnization)
            # Filtering the leads to the current agent
            queryset = queryset.filter(agent__user = user)
        return queryset


class LeadCreate(OrgarnizerCheckLoginRequiredMixin,generic.CreateView):
    template_name = 'Leads/lead_create.html'
    form_class = CreateLead

    def form_valid(self,form):
        lead_profile = form.save(commit=False)
        lead_profile.orgarnization = self.request.user.userprofile
        lead_profile.save()
        return super(LeadCreate,self).form_valid(form)

    def get_success_url(self):
        return reverse('lead_list')


class LeadUpdate(OrgarnizerCheckLoginRequiredMixin,generic.UpdateView):
    context_object_name = 'lead_detail'
    template_name = 'Leads/lead_update.html'
    form_class = CreateLead

# Filtering the leads to the current profile
    def get_queryset(self):
        user = self.request.user
        # Filtering the leads to the current profile
        if user.is_orgarnizer:
            queryset = Lead.objects.filter(orgarnization = user.userprofile)
        return queryset
    def get_success_url(self):
        return reverse('lead_list')


class LeadDelete(OrgarnizerCheckLoginRequiredMixin,generic.DeleteView):
    template_name = 'Leads/lead_delete.html'
    context_object_name = 'lead_detail'

# Filtering the leads to the current profile
    def get_queryset(self):
        user = self.request.user
        # Filtering the leads to the current profile
        if user.is_orgarnizer:
            queryset = Lead.objects.filter(orgarnization = user.userprofile)
        return queryset

    def get_success_url(self):
        return reverse('lead_list')


class AssignLeadsToAgents(OrgarnizerCheckLoginRequiredMixin,generic.FormView):
    template_name = 'Leads/assign_leads.html'
    context_object_name = 'lead_detail'
    form_class = AssignLeadToAgent

    def get_form_kwargs(self,**kwargs):
        kwargs = super(AssignLeadsToAgents,self).get_form_kwargs(**kwargs)
        kwargs.update({'request' : self.request})
        return kwargs

    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id = self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignLeadsToAgents,self).form_valid(form)

    def get_success_url(self):
        return reverse('lead_list')