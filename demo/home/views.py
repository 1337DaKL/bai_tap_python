from django.shortcuts import render


def get_home(request):
    return render(request, 'home/homect.html')
# Create your views here.
