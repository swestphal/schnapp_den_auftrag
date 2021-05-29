from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.job.models import Job


# Create your views here.
def frontpage(request):
    jobs = Job.objects.all()[0:3]
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
            if account_type == 'employer':
                user.userprofile.is_employer = True
                user.userprofile.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, "core/signup.html", context)
