from django.urls import path
from .import views

urlpatterns = [
    path('', views.hi, name='Home-Page'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]