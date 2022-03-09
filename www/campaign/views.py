from django.shortcuts import render
from django.http import HttpResponse
from .models import Organizer, Fundraiser, Update, Comment, Contribution
from datetime import datetime
from django.views import generic


class FundraiserListView(generic.ListView):
    model = Fundraiser


def index(request):
    fundraisers = []
    for fr in Fundraiser.objects.all():
        t_donations = 0
        for c in Contribution.objects.filter(fundraiser__exact=fr.id):
            t_donations += c.amount
        fundraiser = {
            'name': fr.title,
            'organizer': fr.organizer.__str__(),
            'total_raised': t_donations,
        }
        fundraisers.append(fundraiser)
    return render(request, 'index.html', context={'fundraisers': fundraisers})


def about(request):
    context = {}
    return render(request, 'about.html', context=context)
