from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/',  auth_view.LoginView.as_view(authentication_form=LoginForm, template_name='core/login.html'), name='login')
]
