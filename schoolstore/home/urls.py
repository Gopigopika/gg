from . import views

from django.urls import path

urlpatterns = [

   path('',views.home,name='home'),
   path('register',views.register,name='register'),
   path('login', views.login, name='login'),
   path('llg',views.llg,name='llg'),
   path('logout', views.logout, name='logout'),
   path('re',views.re,name='re'),
   path('gg',views.gg,name='gg'),

]
