from django.shortcuts import render
from django.http import HttpResponse
from .models import Jobs

def encontrar_jobs(request):
    if request.method == 'GET':
        jobs = Jobs.objects.filter(reservado=False)
        print(jobs)
        return render(request, 'encontrar_jobs.html')
