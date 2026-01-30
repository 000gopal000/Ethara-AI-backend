from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer
from django.db import IntegrityError

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        employee_id = request.data.get('employee')
        date = request.data.get('date')
        if Attendance.objects.filter(employee=employee_id, date=date).exists():
           return Response({"error": "Attendance already marked for this date"}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def by_employee(self, request):
        emp_id = request.query_params.get('employee_id')
        if emp_id:
             attendance = Attendance.objects.filter(employee__employee_id=emp_id)
             serializer = self.get_serializer(attendance, many=True)
             return Response(serializer.data)
        return Response({"error": "Employee ID required"}, status=status.HTTP_400_BAD_REQUEST)
