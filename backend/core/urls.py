from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('donors/', views.donor_list, name='donor_list'),
    path('donors/create/', views.donor_create, name='donor_create'),
    path('donors/<int:pk>/edit/', views.donor_edit, name='donor_edit'),
    path('donors/<int:pk>/delete/', views.donor_delete, name='donor_delete'),
    path('ngocampaigns/', views.ngocampaign_list, name='ngocampaign_list'),
    path('ngocampaigns/create/', views.ngocampaign_create, name='ngocampaign_create'),
    path('ngocampaigns/<int:pk>/edit/', views.ngocampaign_edit, name='ngocampaign_edit'),
    path('ngocampaigns/<int:pk>/delete/', views.ngocampaign_delete, name='ngocampaign_delete'),
    path('volunteers/', views.volunteer_list, name='volunteer_list'),
    path('volunteers/create/', views.volunteer_create, name='volunteer_create'),
    path('volunteers/<int:pk>/edit/', views.volunteer_edit, name='volunteer_edit'),
    path('volunteers/<int:pk>/delete/', views.volunteer_delete, name='volunteer_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
