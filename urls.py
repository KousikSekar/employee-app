from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('employee', views.EmployeeViewSet, basename='employee')
router.register('department', views.DepartmentViewSet, basename = 'department')
#
# urlpatterns = [
#     path('',include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

urlpatterns =[
    # path('employee', views.EmployeeList),
    path('', include(router.urls)),
]