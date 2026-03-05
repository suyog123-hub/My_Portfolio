
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('about/',about,name='about'),
     path('contact/',contact,name='contact'),
      path('',home,name='home'),
       path('project/',project,name='project'),
         path('skills/',skills,name='skills'),
             path('main/',main,name='main'),
           path('testionomial/',testinomial,name='testinomial'),
 ]
