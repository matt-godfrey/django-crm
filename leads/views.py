from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def home_page(request):
    # return HttpResponse("Hello, world!")
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "home_page.html", context)


