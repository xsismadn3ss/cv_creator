from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CV
from django.urls import reverse


@login_required()
def create(request: HttpRequest):
    if request.method == "POST":

        user = User.objects.get(id=request.user.id)

        name = f"{user.first_name} {user.last_name}"
        email = user.email
        phone = request.POST.get("phone")
        urls = request.POST.get("urls")
        job = request.POST.get("job")
        about = request.POST.get("about")
        exp = request.POST.get("exp")
        education = request.POST.get("education")
        top = request.POST.get("top")
        soft = request.POST.get("soft")
        lang = request.POST.get("lang")

        new_cv = CV(
            name=name,
            email=email,
            phone=phone,
            urls=urls,
            job=job,
            about=about,
            exp=exp,
            edu=education,
            top_skills=top,
            soft_skills=soft,
            lang=lang,
            user=request.user,
        )
        new_cv.save()

        cv = CV.objects.last()
        return redirect(reverse("result", args=[cv.id]))

    else:
        return render(request, "create.html")


@login_required()
def result(request: HttpRequest, id):
    cv = get_object_or_404(CV, id=id, user=request.user.id)
    links = cv.urls.split(",")
    edu = cv.edu.split(",")
    top = cv.top_skills.split(",")
    soft = cv.soft_skills.split(",")
    lang = cv.lang.split(",")
    return render(request, "result.html", {"cv": cv, "links": links, "edu": edu, 'top':top, 'soft':soft, 'lang':lang})

def dashboard(request:HttpRequest):
    cv_list = CV.objects.filter(user=request.user.id).values()
    return render(request, 'dashboard.html', {'cvList':cv_list})