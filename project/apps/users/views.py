
# Create your views here.
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from users.models import User, Group
from datetime import datetime


def main(request):
    return render(request, 'main.html')


def show_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def show_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def add_page_groups(request):
    return render(request, 'add_groups.html')


def add_page_users(request):
    groups = Group.objects.all()
    return render(request, 'add_users.html', {'groups': groups})


def users_add(request):

    a = User(user_name=request.POST['Name'], slug=request.POST['Slug'],
             group=Group.objects.get(group_name=request.POST['Group']))
    a.save()
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def groups_add(request):
    a = Group(group_name=request.POST['Name'], slug=request.POST['Slug'],
              group_description=request.POST['Description'])
    a.save()
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def delete_group(request, slug):
    a = Group.objects.filter(slug=slug).delete()
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def delete_user(request, slug):
    a = User.objects.filter(slug=slug).delete()
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def edit_page_users(request, slug):
    a = User.objects.get(slug=slug)
    groups = Group.objects.all()
    return render(request, 'edit_page_users.html', {'user': a, 'groups': groups})


def users_update(request, slug):
    a = User.objects.filter(slug=slug).update(user_name=request.POST['Name'], slug=request.POST['Slug'],
                                                  group=Group.objects.get(group_name=request.POST['Group']),
                                              created=datetime.now())
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def edit_page_groups(request, slug):
    a = Group.objects.get(slug=slug)
    return render(request, 'edit_page_groups.html', {'group': a})


def groups_update(request, slug):
    a = Group.objects.filter(slug=slug).update(group_name=request.POST['Name'], slug=request.POST['Slug'],
                                              group_description=request.POST['Group description'])
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})