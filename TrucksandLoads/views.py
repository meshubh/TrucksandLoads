from django.shortcuts import render
from models import *
from rest_framework.response import Response
from forms import *
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
def home(request):
    template = get_template("home.html")
    return HttpResponse(template.render())



def truck_list(request):
    """
      List all snippets, or create a new snippet.
      """
    q=Trucks.objects.all()
    template = get_template("style.html")
    if request.method == 'POST':
        truck_form = TruckForm(data=request.POST)
        truck_form.save()
    else:
        truck_form=TruckForm()
    return HttpResponse(template.render(context={'list': q, 'truck_form': truck_form},
                                        request=request))


def load_list(request):
    """
      List all snippets, or create a new snippet.
      """
    q=Load.objects.all()
    template = get_template("load.html")
    if request.method == 'POST':
        load_form = LoadForm(data=request.POST)
        load_form.save()
    else:
        load_form=LoadForm()
    return HttpResponse(template.render(context={'list': q, 'load_form': load_form},
                                        request=request))