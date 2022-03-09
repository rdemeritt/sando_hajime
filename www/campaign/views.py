from django.shortcuts import render
from django.http import HttpResponse
from .models import Organizer, Fundraiser, Update, Comment, Contribution
from datetime import datetime


def index(request):
    num_fundraisers = Fundraiser.objects.all().count()
    # count the total donations
    t_donations = 0
    for fr in Fundraiser.objects.all():
        for c in Contribution.objects.filter(fundraiser__exact=fr.id):
            t_donations += c.amount

    # get and set last visited
    last_visited = request.session.get('last_visited', str(datetime.now()))
    request.session['last_visited'] = str(datetime.now())

    context = {
        'num_fundraisers': num_fundraisers,
        'total_raised': t_donations,
        'last_visited': last_visited,
    }
    return render(request, 'index.html', context=context)
