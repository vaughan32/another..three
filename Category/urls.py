from django.urls import path
from . import views

urlpatterns = [
    path('category_list/',views.CategoryRelatedToLeadListView.as_view(), name='category_list'),
    path('category_create/',views.CreateCategory.as_view(), name='category_create'),
    path('category_detail/<int:pk>/',views.CategoryRelatedToLeadDetailView.as_view(), name='category_detail_related_to_leads'),
    path('category_update/<int:pk>/',views.CategoryRelatedToLeadUpdateView.as_view(), name='category_update_related_to_leads'),
    path('category_updateform/<int:pk>/',views.UpdateCategory.as_view(), name='category_update'),
    path('category_delete/<int:pk>/',views.DeleteCategory.as_view(), name='category_delete'),

]
