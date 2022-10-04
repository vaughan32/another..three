from django.urls import path
from . import views as template_views

urlpatterns = [
    path('lead_list/',template_views.LeadList.as_view(),name='lead_list'),
    path('lead_create/',template_views.LeadCreate.as_view(),name='lead_create'),
    path('lead_detail/<int:pk>/',template_views.LeadDetails.as_view(),name='lead_detail'),
    path('lead_update/<int:pk>/',template_views.LeadUpdate.as_view(),name='lead_update'),
    path('lead_delete/<int:pk>/',template_views.LeadDelete.as_view(),name='lead_delete'),
    path('lead_assign/<int:pk>/',template_views.AssignLeadsToAgents.as_view(),name='assign_leads')]
