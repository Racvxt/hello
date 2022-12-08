from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="Home"),
    path('about/',views.jkl,name='basic'),
    path('test/',views.test,name='testing'),
    path('sum/',views.addition,name='add'),
    path('format/',views.format,name='format'),
    path('xello',views.xello,name="xello"),
    path('vb/',views.vb,name="vb"),
    path('testing/',views.testing,name="testing"),
    path('forauth/',views.forauth,name="forauth"),
    path('pagal/', views.pagal,name='pagal')
    
    
    
]