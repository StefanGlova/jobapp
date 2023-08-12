from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost

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

class TempClass:
    x = 5

# Create your views here.

def hello(request):
    # template = loader.get_template("app/hello.html")
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    age = 25
    context = {"name": "Django", "first_list": list,
               "temp_object": temp, "age": age,
               "is_authenticated": is_authenticated}
    # return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context)


def jobs_list(request):
    # job_list = "<ul>"
    # for job in job_title:
    #     job_id = job_title.index(job)
    #     detail_url = reverse("jobs_detail", args=(job_id,))
    #     job_list += f"<li><a href='{detail_url}'>{job}</a></li>"
    # job_list += "</ul>"
    # return HttpResponse(job_list)
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse("jobs_home"))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # context = {"jobtitle": job_title[id], "job_description": job_description[id]}
        job = JobPost.objects.get(id=id)
        context = {"job": job}
        return render(request, "app/job_detail.html", context)
        # return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Not Found")
