from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from UserInfo.models import Fraternity
from PartyList.models import Party

@login_required(login_url='login/')
def index(request):
    # Is this user a manager?
    managers = Fraternity.managers()
    is_manager = request.user in managers

    if is_manager:
        parties = Party.objects.filter(fraternity=request.user.fraternity).order_by("-date")
        context = {'parties': parties}
        return render(request, 'manager_home.html', context)

    return redirect('parties')
