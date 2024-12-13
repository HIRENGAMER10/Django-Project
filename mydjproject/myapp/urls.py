from django.urls import path
from . import views
urlpatterns = [
    path("",views.homepage),
    path("home",views.homepage),
    path("add-student",views.addStudent),
    path("display-student",views.displayStudent),
    path("about",views.aboutpage),
    path("contact",views.contactpage),
    path("form",views.formpageview),
    path("process",views.formpageprocess),
]