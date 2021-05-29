from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    context = {
        'userprofile': request.user.userprofile
    }
    return render(request, 'userprofile/dashboard.html', context)
