from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.Index, name='home'),
    path('accounts/login/', view=views.login_view, name='login'),
    path('accounts/signup/', view=views.signup, name='signup'),
    path('accounts/logout/', view=views.signout, name='logout'),
    path('accounts/', view=views.account, name='account'),
    path('accounts/edit', view=views.edit_account, name='edit_account')
]
