from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.job.models import Application, Job


# Create your views here.

@login_required
def dashboard(request):
    context = {
        'userprofile': request.user.userprofile
    }
    return render(request, 'userprofile/dashboard.html', context)


@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    context = {
        'application': application
    }
    return render(request, 'userprofile/view_application.html', context)


@login_required
def view_dashboard_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)
    context = {
        'job': job
    }
    return render(request, 'userprofile/view_dashboard_job.html', context)
