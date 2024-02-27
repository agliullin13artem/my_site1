from django.shortcuts import render, redirect
from .models import Employee
from datetime import datetime

# отметка посещаймости
def mark_attendance(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        arrival_time = datetime.now()  # Записываем текущую дату и время прихода

        employee = Employee.objects.create(
            first_name=first_name, last_name=last_name, arrival_time=arrival_time
        )
        employee.save()

    employees = Employee.objects.all()

    return render(request, "proga/attendance.html", {"employees": employees})

# отметьте отправление
def mark_departure(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.departure_time = datetime.now()  # Записываем текущую дату и время ухода
    employee.save()

    return redirect("mark_attendance")

# калькулятор часов
def calculate_working_hours(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    working_hours = (
        employee.departure_time - employee.arrival_time
    )  # Рассчитываем отработанное время

    return render(request, "proga/working_hours.html", {"working_hours": working_hours})
