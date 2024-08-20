from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def create(request:HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        if True:
            pass

    else:
        # form = CV_form()
        return render(request, "create.html")
