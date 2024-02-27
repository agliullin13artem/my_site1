from django.urls import path
from .views import mark_attendance, mark_departure, calculate_working_hours

urlpatterns = [
    path('', mark_attendance, name='mark_attendance'),
    path('mark_departure/<int:employee_id>/', mark_departure, name='mark_departure'),
    path('calculate_working_hours/<int:employee_id>/', calculate_working_hours, name='calculate_working_hours'),
]