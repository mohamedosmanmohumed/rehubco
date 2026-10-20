from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('executive/', views.executive_dashboard, name='executive_dashboard'),
    path('tendering/', views.tendering_dashboard, name='tendering_dashboard'),
    path('engineering/', views.engineering_dashboard, name='engineering_dashboard'),
    path('procurement/', views.procurement_dashboard, name='procurement_dashboard'),
    path('finance/', views.finance_dashboard, name='finance_dashboard'),
    path('hr/', views.hr_dashboard, name='hr_dashboard'),
    path('projects/', views.project_pipeline, name='project_pipeline'),
    path('inventory/', views.inventory_grid, name='inventory_grid'),
    path('branches/', views.branch_selector, name='branch_selector'),
]
