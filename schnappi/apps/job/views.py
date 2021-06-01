from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddJobForm, ApplicationForm
from .models import Job
from apps.notification.utilities import create_notification


# Create your views here.
def search(request):
    return render(request, 'job/search.html')


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    context = {
        'job': job
    }
    return render(request, 'job/job_detail.html', context)


@login_required
def apply_for_job(request, job_id):
    print("------")
    job = Job.objects.get(pk=job_id)
    print(job)
    print(request.method)
    if request.method == 'POST':

        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            create_notification(request, job.created_by, 'application', extra_id=application.id)

            return redirect('dashboard')
    else:
        form = ApplicationForm()
        context = {
            'form': form,
            'job': job
        }
    return render(request, 'job/apply_for_job.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')

    else:
        form = AddJobForm()

    context = {
        'form': form
    }
    return render(request, 'job/add_job.html', context)
