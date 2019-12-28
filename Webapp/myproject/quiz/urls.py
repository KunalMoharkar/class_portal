from django.urls import path,re_path
from . import views

app_name = 'quiz'  # here for namespacing of urls.

urlpatterns =  [
    path("homepage/", views.homepage, name="homepage"),
    path("logout/",views.userlogout, name="logout"),
    path("register/", views.UserFormView.as_view(), name="register"),
    path("", views.userlogin, name="login"),
    re_path(r'^homepage/(?P<que_id>[0-9]{1})/check/$', views.check, name="check"),
    re_path(r'^homepage/(?P<que_id>[0-9]{1})/$', views.details, name="details")

]