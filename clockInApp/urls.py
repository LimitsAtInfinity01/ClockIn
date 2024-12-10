from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('clockIn', views.clockIn, name='clockIn'),
    path('clockOut', views.clockOut, name='clockOut'),
    path('printPDF', views.printPDF, name='printPDF'),
    path('reports', views.reports, name='reports')
]