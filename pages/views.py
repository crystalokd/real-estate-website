from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, lga_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]

    context = {
        'listings': listings,
        'lga_choices': lga_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_relators = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_relators
    }

    return render(request, 'pages/about.html', context)