from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    name = 'Mark'
    return render(request, 'index.html', {'name':name})


def counter(request):
    # Safely get the 'text' parameter from the request, defaulting to an empty string if it's not provided
    text = request.GET.get('text', '')
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
