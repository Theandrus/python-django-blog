from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.main, name='main'),
    path('groups/', views.show_groups, name='show_groups'),
    path('users/', views.show_users, name='show_users'),
    path('users/add/', views.add_page_users, name='add_page_users'),
    path('groups/add/', views.add_page_groups, name='add_page_groups'),
    path('groups/add/added', views.groups_add, name='groups_add'),
    path('users/add/added', views.users_add, name='users_add'),
    path('users/<slug:slug>/delete', views.delete_user, name='delete_user'),
    path('groups/<slug:slug>/delete', views.delete_group, name='delete_group'),
    path('users/<slug:slug>/edit', views.edit_page_users, name='edit_page_users'),
    path('users/<slug:slug>/edit/edited', views.users_update, name='users_update'),
    path('groups/<slug:slug>/edit/', views.edit_page_groups, name='edit_page_groups'),
    path('groups/<slug:slug>/edit/edited', views.groups_update, name='groups_update'),

]