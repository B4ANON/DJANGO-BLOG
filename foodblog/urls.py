
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('base',base,name="base"),
    path('singleblog/<slug>',singleblog,name="singleblog"),
    path('aboutus',aboutus,name="aboutus"),
    path('searched',searched,name="searched"),
]
