from django.urls import path
from .views import job_detail, add_job

urlpatterns = [
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('add/', add_job, name='add_job')
]
