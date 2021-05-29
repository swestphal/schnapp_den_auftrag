from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddJobForm
from .models import Job


# Create your views here.


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    context = {
        'job': job
    }
    return render(request, 'job/job_detail.html', context)


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
