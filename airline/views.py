from django.shortcuts import render
from .models import Flight, Airport

# Create your views here.

def index(request):
    return render(request, "airline/index.html", {
        "airline": Flight.objects.all()
    })
 