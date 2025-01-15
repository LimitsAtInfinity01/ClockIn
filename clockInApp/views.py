import django
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse

from clockInApp.forms import RegisterEmployeeForm, ClockInForm, ClockOutForm, ReportForm
from clockInApp.models import Employee, Admins, Times

from django.db.models import DateField
from django.db.models.functions import Cast

import datetime

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 

import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
def index(request):
    times = Times.objects.all()
    print(times)
    return render(request, "clockInApp/index.html", {
        'times': times
        })

def register(request):
    if request.method == 'POST':
        form = RegisterEmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastName = form.cleaned_data['lastName']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            employee = Employee(name=name,
                                lastName=lastName,
                                username=username)
            employee.set_password(password)
            #TODO check if employee already exists before saving
            try: 
                employee.save()
                return redirect('index')
            except django.db.utils.IntegrityError:
                # TODO display an error message when employee exits
                return redirect('register')
    else:
        form = RegisterEmployeeForm()
    return render(request, "clockInApp/register.html",{
        'form': form
    })

def clockIn(request):
    if request.method == 'POST':
        form = ClockInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                employee = Employee.objects.get(username=username)
            except Employee.DoesNotExist:
                print('Employ does not exists')
                return redirect('clockIn')

            password_correct = employee.check_password(password)
            print(datetime.date.today())
            if password_correct:
                #TODO time it's wrong. Fix it!
                if not employee.signedIn:
                    now = datetime.datetime.now()
                    clockIn = Times(employee=employee,
                                    timeIn=now)
                    
                    employee.signedIn = True
                    print("You are clocked in")
                    employee.save()
                    clockIn.save()
                    return redirect('index')
                else:
                    print('You are already signed in!')
                    return redirect('index')
            else:
                print('Password incorrect')
    else:
        form = ClockInForm()

    return render(request, 'clockInApp/clockIn.html',{
        'form': form
    })

def clockOut(request):
    if request.method == 'POST':
        form = ClockOutForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                employee = Employee.objects.get(username=username)
            except Employee.DoesNotExist:
                print('Employee does not exist')
                return redirect('index')

            if not employee.check_password(password):
                print('Incorrect Password')
                return redirect('index')

            # Fetch the most recent Times record for the employee where timeOut is not set
            time = Times.objects.filter(employee=employee, timeOut__isnull=True).order_by('-timeIn').first()

            if not time:
                print("No active clock-in record found. You need to clock in first.")
                return redirect('index')

            if employee.signedIn:
                # Update timeOut for the most recent record
                time.timeOut = datetime.datetime.now()
                time.save()
                employee.signedIn = False
                employee.save()

                print(f"Clocked out successfully at: {time.timeOut}")
                return redirect('index')
            else:
                print('You are not clocked in')
                return redirect('index')
    else:
        form = ClockOutForm()

    return render(request, "clockInApp/clockOut.html", {
        'form': form
    })

def printPDF(request):
    pass
#     doc = SimpleDocTemplate("example_platypus.pdf")
#     styles = getSampleStyleSheet()
#     content = []
#     content.append(Paragraph("This is a paragraph.", styles['Normal']))
#     content.append(Spacer(1, 12))

#     times = Times.objects.all()
#     print(times)
#     data = [["Name", "Last name", "Clock in", "Clock out", "Date"]]
#     for time in times:
#         if time.timeOut:
#             clock_In = time.timeIn.strftime('%H:%M')
#             clock_out = time.timeOut.strftime('%H:%M')
#             data.append([time.employee.name, time.employee.lastName, clock_In, clock_out, time.date])
#         else:
#             clock_In = time.timeIn.strftime('%H:%M')
#             data.append([time.employee.name, time.employee.lastName, clock_In, '', time.date])

#     table = Table(data)
#     content.append(table)

#     doc.build(content)
#     return redirect('index')

def myWorkHistory(request):
    times = None
    if request.method ==  'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['username'] = username
            password = form.cleaned_data['password']
            employee = Employee.objects.get(username=username)
            if employee.check_password(password):
                times = Times.objects.filter(employee=employee.id).select_related('employee').all()

                time_list_with_name = []
                for time in times:
                    time_list_with_name.append({
                        'first_name': time.employee.name,
                        'last_name': time.employee.lastName,
                        "timeIn": time.timeIn,
                        "timeOut": time.timeOut,
                        'workedTime': time.worked_time
                    })
                return JsonResponse(time_list_with_name, safe=False)
            else:
                return redirect('index')
    else:
        form = ReportForm()
    return render(request, 'clockInApp/myWorkHistory.html', {
        'form': form,
    })

# http://127.0.0.1:8000/
def searchBox_API(request):
    # mm-dd-yyyy
    #TODO Implement a search that covers a range of dates
    search_date = request.GET.get('q')
    month, day, year = search_date.split('-')
    username = request.session.get('username')
    employee = Employee.objects.get(username=username)

    # Not returning all the data. There is a discrepancy in the database
    times = Times.objects.annotate(date_only=Cast('timeIn', DateField())).filter(employee=employee, date_only=datetime.date(int(year), int(month), int(day)))

    data = []
    for time in times:
        print(time.employee.name)
        print(time.employee.lastName)
        print(time.timeIn)
        print(time.timeOut)
        print(time.worked_time)
        data.append({
            'first_name': time.employee.name,
            'last_name': time.employee.lastName,
            "timeIn": time.timeIn,
            "timeOut": time.timeOut,
            'workedTime': time.worked_time
        })
       
    return JsonResponse(data, safe=False)


def example_page(request):
    return render(request, 'clockInApp/example.html')