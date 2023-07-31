from django.http import HttpResponse
from django.shortcuts import render, redirect

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
        job_list += f"<li><a href='job/{job_id}'>{job}</a></li>"
    job_list += "</ul>"
    
    return HttpResponse(job_list)

def job_detail(request, id):
    if id == 0:
        return redirect("/")
    return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
    return HttpResponse(return_html)
