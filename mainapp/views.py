from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "wrapper.html")


def titan(request):
    return render(request, "titan.html")