from django.urls import path
from app import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about/",views.about,name="about")
]
    