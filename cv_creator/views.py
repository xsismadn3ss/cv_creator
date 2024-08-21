from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CV


@login_required()
def create(request:HttpRequest):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        urls = request.POST.get("urls")
        job = request.POST.get("job")
        about = request.POST.get("about")
        exp = request.POST.get("exp")
        education = request.POST.get("education")
        top = request.POST.get("top")
        soft = request.POST.get("soft")
        lang = request.POST.get("lang")

        new_cv = CV(name=name, email=email, phone=phone, urls = urls, job = job, about = about, exp = exp, edu= education, top_skill = top, soft_skills = soft, lang = lang)

        return HttpResponse("Datos enviados con exito!")
        # return HttpResponseRedirect('create/add_exp')

    else:
        return render(request, "create.html")


def result(request:HttpResponse):
    return HttpResponse("Datos enviados con exito")
