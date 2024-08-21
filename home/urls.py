from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.Index, name='home'),
    path('accounts/login/', view=views.login_view, name='login'),
    path('accounts/signup/', view=views.signup, name='signup'),
    path('accounts/logout/', view=views.signout, name='logout')
]
