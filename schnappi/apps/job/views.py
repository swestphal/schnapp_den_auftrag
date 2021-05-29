from django.shortcuts import render
from .models import Job


# Create your views here.


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    context = {
        'job': job
    }
    return render(request, 'job/job_detail.html',context)
