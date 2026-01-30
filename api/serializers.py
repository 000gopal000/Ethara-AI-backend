from rest_framework import serializers
from .models import Employee, Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    attendance_records = AttendanceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Employee
        fields = ['id', 'employee_id', 'full_name', 'email', 'department', 'created_at', 'attendance_records']
