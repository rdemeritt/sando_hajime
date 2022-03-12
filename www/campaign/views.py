from django.shortcuts import render
from django.http import HttpResponse
from .models import Fundraiser, Contribution
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    fundraisers = []
    for fr in Fundraiser.objects.all():
        t_donations = 0
        for c in Contribution.objects.filter(fundraiser__exact=fr.id):
            t_donations += c.amount
        fundraiser = {
            'name': fr.title,
            # 'url': fr.get_absolute_url(),
            'organizer': fr.organizer.__str__(),
            'total_raised': t_donations,
        }
        fundraisers.append(fundraiser)
    return render(request, 'index.html', context={'fundraisers': fundraisers})
