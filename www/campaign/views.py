from django.shortcuts import render
from django.http import HttpResponse
from .models import Organizer, Fundraiser, Update, Comment, Contribution


def index(request):
    num_fundraisers = Fundraiser.objects.all().count()

    context = {
        'num_fundraisers': num_fundraisers
    }
    return render(request, 'index.html', context=context)
