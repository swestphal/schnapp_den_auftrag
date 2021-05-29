from django.shortcuts import render


# Create your views here.
def frontpage(request):
    return render(request, "core/base.html")

def signup(request):
    return render(request, "core/signup.html")