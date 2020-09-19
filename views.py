from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from . import serializers, models

from rest_framework.decorators import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from drf_multiple_model.views import ObjectMultipleModelAPIView


# class DepartmentViews(viewsets.ModelViewSet):
#     queryset = Department.objects.all().order_by('dept_id')
#     serializer_class = DepartmentSerializer

# Create your views here.

# def EmployeeList(request):
#     if request.method == 'GET':
#         list = Employees.objects.all()
#         serializer = EmployeeSerializer(list, many=True)
#         return JsonResponse(serializer.data, status=200, safe=False)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employees.objects.all()


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()

    # {'queryset':Department.objects.all(), 'serializer_class': DepartmentSerializer},
    # {'queryset':Employee_Contact.objects.all(), 'serializer_class': ContactSerializer },
    # {'queryset':Employees.objects.all(), 'serializer_class': EmployeeSerializer}
