from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('clockIn', views.clockIn, name='clockIn'),
    path('clockOut', views.clockOut, name='clockOut'),
    path('printPDF', views.printPDF, name='printPDF'),
    path('myWorkHistory', views.myWorkHistory, name='myWorkHistory'),
    path('example-view/', views.example_view, name='example-view'),
    path('example-page/', views.example_page, name='example-page')
]