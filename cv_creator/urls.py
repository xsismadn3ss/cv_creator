from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.dashboard, name="dashboard"),
    path(route='create', view=views.login_required(views.create), name='create'),
    path(route='result/<int:id>', view=views.result, name="result"),
    path(route='edit/<int:id>', view=views.edit, name="edit")
]
