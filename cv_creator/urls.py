from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.login_required(views.create), name='create'),
    path(route='result/', view=views.result, name="result")
]
