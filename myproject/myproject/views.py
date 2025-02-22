from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature 

# Create your views here.
def index (request):
   features = Feature.objects.all()
   return render(request, 'index.html', {'features' : features})


def counter(request):
    # Safely get the 'text' parameter from the request, defaulting to an empty string if it's not provided
    text = request.POST['text']
    amount_of_words = len(text.split())   
    return render(request, 'counter.html', {'text': text})
 
 



