from django.urls import path
from .views import *
urlpatterns = [
    path('',Home,name="home"),
    path('contact/', Contact,name="contact"),
    path('about_us/', AboutUs,name="about_us"),
    path('tracking/', TrackingPage,name="tracking"),
    path("ask/", AskPage, name="ask"),
    path("questions/",QuestionsgPage, name="questions")
]