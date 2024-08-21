from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .functions import trim


# Create your views here.
def create(request:HttpRequest):
    if request.method == "POST":
        # personal
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        urls = request.POST.get("urls")
        # description
        job = request.POST.get("job")
        about = request.POST.get("about")
        exp = request.POST.get("exp")
        education = request.POST.get("education")
        # skills
        top = request.POST.get("top")
        soft = request.POST.get("soft")
        lang = request.POST.get("lang")

        data = trim(name,email, phone, urls, job, about, exp, education, top, soft, lang)
        print(data)

        return HttpResponse("Datos recibidos correctamente")

    else:
        return render(request, "create.html")