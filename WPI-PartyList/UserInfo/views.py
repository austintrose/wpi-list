from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.html import strip_tags

from UserInfo import utils
from UserInfo.models import UserInfo, EditUserInfoForm

def users(request):
    if request.user.fraternity.manager == request.user:
        managed_users = request.user.fraternity.brothers()
        return render(request, 'users.html', {'users': managed_users})

@permission_required('UserInfo.manage_users', login_url='Secure.views.index')
def add_users(request):
    """
        Provides a view for adding a user
    """
    context = {
        'message': []
    }

    if request.method == 'POST':
        add_type = request.POST['type']

        if add_type == "SINGLE":
            to_add = strip_tags(request.POST['username'])
            first_name = strip_tags(request.POST['firstname'])
            last_name = strip_tags(request.POST['lastname'])
            major = strip_tags(request.POST['major'])
            year = strip_tags(request.POST['class'])

            exists = User.objects.filter(username=to_add).count()
            if exists:
                context['message'].append("Username " + to_add + " is taken.")
            else:
                try:
                    utils.create_user(to_add, first_name, last_name, major, year)
                    context['message'].append("User " + to_add + " successfully added.")
                except:
                    context['message'].append("Error adding " + to_add + ".")
    return render(request, 'secure/add_users.html', context)

@permission_required('UserInfo.manage_users', login_url='Secure.views.index')
def manage_users(request):
    """
        Provides a view to manage all of the users in the system.
    """

    all_users = User.objects.all().order_by("last_name")

    context = {
        'all_users': all_users
    }

    return render(request, 'secure/manage_users.html', context)

@permission_required('UserInfo.manage_users', login_url='Secure.views.index')
def reset_password(request, user):
    """
        Resets a single user's password.
    """

    # TODO: This should be changed over to being a POST request in the future.
    requested_user = User.objects.get(username__exact=user)

    utils.reset_password(requested_user)

    return redirect("UserInfo.views.manage_users")

@login_required
def edit_user(request, user):
    """
        Provides a view to edit a single user.
    """
    requested_user = User.objects.get(username__exact=user)
    if (not requested_user == request.user) and not request.user.is_staff:
        return redirect('PubSite.views.permission_denied')

    if request.method == 'POST':
        form = EditUserInfoForm(request.POST, instance=requested_user.userinfo)
        if form.is_valid():
            form.save()
            return redirect("UserInfo.views.manage_users")
    else:
        form = EditUserInfoForm(instance=requested_user.userinfo)



    context = {
        'requested_user': requested_user,
        'form': form,
        'error': form.errors
    }

    return render(request, 'secure/edit_user.html', context)

@login_required
def change_password(request):
    """
        Provides a view where a user can change their change_password
    """

    context = {
        'message': []
    }

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            context['message'].append("Password successfully changed.")
        else:
            context['message'].append("Error changing password.  Check that your passwords match and that your old password is correct.")

    context['form'] = PasswordChangeForm(user=request.user)

    return render(request, 'secure/reset_password.html', context)

