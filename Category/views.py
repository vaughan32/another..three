from django.urls import reverse
from Leads.models import Lead,Category
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from Agents.mixins import OrgarnizerCheckLoginRequiredMixin
from Category.forms import CategoryLead,CreateCategoryForm
class CategoryRelatedToLeadListView(LoginRequiredMixin,generic.ListView):
    template_name = 'Category/category_lead_list.html'
    context_object_name = 'category_lead_list'

# Filtering the category to the current profile and agent
    def get_queryset(self):
        user = self.request.user
        # Filtering the category to the current profile
        if user.is_orgarnizer:
            queryset = Category.objects.filter(orgarnization = user.userprofile)
        else:
            # Filtering the category to the current agent orgarnization
            queryset = Category.objects.filter(orgarnization = user.agent.orgarnization)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryRelatedToLeadListView,self).get_context_data(**kwargs)
        user = self.request.user
        # Filtering the category to the current profile
        if user.is_orgarnizer:
            queryset = Lead.objects.filter(orgarnization = user.userprofile)
        else:
            # Filtering the category to the current agent orgarnization
            queryset = Lead.objects.filter(orgarnization = user.agent.orgarnization)
        context.update({'leads_under_category_not_assigned' : queryset.filter(category__isnull=True).count()})
        return context


class CategoryRelatedToLeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'Category/category_lead_detail_list.html'
    context_object_name = 'category_detail'

# Filtering the category to the current profile and agent
    def get_queryset(self):
        user = self.request.user
        # Filtering the category to the current profile
        if user.is_orgarnizer:
            queryset = Category.objects.filter(orgarnization = user.userprofile)
        else:
            # Filtering the category to the current agent orgarnization
            queryset = Category.objects.filter(orgarnization = user.agent.orgarnization)
        return queryset


    def get_context_data(self, **kwargs):
        context =  super(CategoryRelatedToLeadDetailView,self).get_context_data(**kwargs)
        user = self.request.user
        # Filtering the category to the current profile
        if user.is_orgarnizer:
            queryset = Lead.objects.filter(orgarnization = user.userprofile)
        else:
            # Filtering the category to the current agent orgarnization
            queryset = Lead.objects.filter(orgarnization = user.agent.orgarnization)
        
        context.update({
            'leads' : queryset.filter(category=self.get_object()),
            'count' : queryset.filter(category=self.get_object()).count()
        })
        return context  
    

class CategoryRelatedToLeadUpdateView(LoginRequiredMixin,generic.UpdateView):
    context_object_name = 'lead_detail'
    template_name = 'Category/category_lead_update_list.html'
    form_class = CategoryLead

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

    def get_success_url(self):
        return reverse('lead_detail', kwargs={'pk' : self.get_object().id}) 


class CreateCategory(OrgarnizerCheckLoginRequiredMixin,generic.CreateView):
    template_name = 'Category/category_create.html'
    form_class = CreateCategoryForm

    def form_valid(self, form):
        profile_orgarnization = form.save(commit=False)
        profile_orgarnization.orgarnization = self.request.user.userprofile
        profile_orgarnization.save()
        return super(CreateCategory,self).form_valid(form)

    def get_success_url(self):
        return reverse('category_list')  


class UpdateCategory(OrgarnizerCheckLoginRequiredMixin,generic.UpdateView):
    template_name = 'Category/category_update.html'
    form_class = CreateCategoryForm
    context_object_name = 'category_detail'

# Filtering the category to the current profile and agent
    def get_queryset(self):
        user = self.request.user
        # Filtering the category to the current profile
        if user.is_orgarnizer:
            queryset = Category.objects.filter(orgarnization = user.userprofile)
        else:
            # Filtering the category to the current agent orgarnization
            queryset = Category.objects.filter(orgarnization = user.agent.orgarnization)
        return queryset


    def get_success_url(self):
        return reverse('category_list')

































class DeleteCategory(OrgarnizerCheckLoginRequiredMixin,generic.DeleteView):
    template_name = 'Category/category_delete.html'
    context_object_name = 'category_detail'

# Filtering the category to the current profile and agent
    def get_queryset(self):
        user = self.request.user
        # Filtering the category to the current profile
        if user.is_orgarnizer:
            queryset = Category.objects.filter(orgarnization = user.userprofile)
        else:
            # Filtering the category to the current agent orgarnization
            queryset = Category.objects.filter(orgarnization = user.agent.orgarnization)
        return queryset

    
    def get_success_url(self):
        return reverse('category_list')