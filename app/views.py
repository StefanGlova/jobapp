from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]

# Create your views here.

def jobs_list(request):
    job_list = "<ul>"
    for job in job_title:
        job_id = job_title.index(job)
        detail_url = reverse("jobs_detail", args=(job_id,))
        job_list += f"<li><a href='{detail_url}'>{job}</a></li>"
    job_list += "</ul>"
    
    return HttpResponse(job_list)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse("jobs_home"))
        return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Not Found")
