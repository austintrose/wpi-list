from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required
from PartyList.models import Party
from django.http import HttpResponse
from PartyList.widgets import PartyForm, EditPartyInfoForm
import json

@login_required
def index(request):
    """
        View for all parties
    """

    parties = Party.objects.all().order_by("date")
    context = {
        'parties': parties,
    }
    return render(request, 'parties.html', context)

@login_required
def guests(request, party):
    """
        View for all guests on the list for a party
    """

    try:
        requested_party = Party.objects.get(pk=party)
    except:
        return redirect("PartyList.views.index")

    partymode = requested_party.isPartyMode()

    context = {
            'party': requested_party,
            'partymode': partymode,
    }

    return render(request, 'partyguests.html', context)


def add_party(request):
    context = {
        'message': []
    }

    if request.method == 'POST':
        form = PartyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.fraternity = request.user.fraternity
            obj.save()
            context['message'].append(obj.name + " successfully added.")
            return redirect('manage_parties')
        else:
            context['message'].append("Error adding party.")

    return render(request, 'add_party.html', context)

def manage_parties(request):
    if request.user.fraternity.manager == request.user:
        all_parties = Party.objects.filter(fraternity=request.user.fraternity).order_by("date").reverse()

    context = {
        'all_parties': all_parties,
    }

    return render(request, 'manage_parties.html', context)

def edit_party(request, party):
    """
        Provides a view to edit a single party.
    """
    # Retrieve the party that we are trying to edit
    try:
        requested_party = Party.objects.get(pk=party)
    except:
        return redirect("PartyList.views.manage_parties")

    errors = None

    if request.method == 'POST':
        # If this is a POST request, the form has been submitted
        form = EditPartyInfoForm(request.POST, request.FILES, instance=requested_party)

        if form.is_valid(): # Check that form is valid
            form.save()
            return redirect("PartyList.views.manage_parties")
    else:
        form = EditPartyInfoForm(instance=requested_party)

    context = {
        'requested_party': requested_party,
        'form': form,
        'error': form.errors
    }

    return render(request, 'edit_party.html', context)

def delete_party(request, party):
    """
        Deletes the party with the ID that is sent in the post request
    """

    if request.method == 'POST':
        try:
            party = Party.objects.get(pk=party)
        except:
            return redirect("PartyList.views.manage_parties")

        party.delete()

    return redirect("PartyList.views.manage_parties")
