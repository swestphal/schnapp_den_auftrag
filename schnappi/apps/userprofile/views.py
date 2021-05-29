from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.job.models import Application

# Create your views here.

@login_required
def dashboard(request):
    context = {
        'userprofile': request.user.userprofile
    }
    return render(request, 'userprofile/dashboard.html', context)


@login_required
def view_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    context = {
        'application': application
    }
    return render(request, 'userprofile/view_application.html', context)
