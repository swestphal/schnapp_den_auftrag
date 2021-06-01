from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.job.models import Job
from apps.userprofile.models import Userprofile


# Create your views here.
def frontpage(request):
    jobs = Job.objects.filter(status=Job.ACTIVE)[0:3]
    context = {
        'jobs': jobs
    }
    return render(request, "core/frontpage.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account_type = request.POST.get('account_type')
            print(account_type)
            if account_type == 'employer':
                print("employer")
                userprofile = Userprofile.objects.create(user=user, is_employer=True)
                userprofile.save()
            else:
                print("jobseeker")
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, "core/signup.html", context)
