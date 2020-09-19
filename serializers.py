from rest_framework import serializers
from .models import Department, Employees, Employee_Contact


#
# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee_Contact
#         fields = '__all__'
#     pass
#
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeContactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Employee_Contact
        fields = ['id', 'address', 'phone', 'employee_id']
        read_only_fields = ('employee_id',)

class EmployeeGetSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(source='dept_id')
    contact = EmployeeContactSerializer(many=True)

    class Meta:
        model = Employees
        fields = ['employee_id', 'first_name', 'last_name', 'doj', 'dob', 'designation', 'dept_id',
                  'department','contact', ]

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(source='dept_id', required=False)
    contact = EmployeeContactSerializer(many=True)

    class Meta:
        model = Employees
        fields = ['employee_id', 'first_name', 'last_name', 'doj', 'dob', 'designation', 'dept_id',
                  'department', 'contact',]
        read_only_fields = ('department',)

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        employee = Employees.objects.create(**validated_data)
        for contact in contact_data:
            Employee_Contact.objects.create(**contact, employee_id=employee, )
        return employee

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.doj = validated_data.get('doj', instance.doj)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.dept_id = validated_data.get('dept_id', instance.dept_id)
        instance.save()
        keep_contacts = []

        for contact in contact_data:
            if 'id' in contact.keys():
                if Employee_Contact.objects.filter(id=contact['id']).exists():
                    c = Employee_Contact.objects.get(id=contact['id'])
                    c.address = contact.get('address', c.address)
                    c.phone = contact.get('phone', c.phone)
                    c.save()
                    keep_contacts.append(c.id)
                else:
                    continue
            else:
                c = Employee_Contact.objects.create(**contact, employee_id=instance)
                keep_contacts.append(c.id)

        return instance

    # def create(self, validated_data):
    #     depts_data = validated_data.pop('depts')
    #     employee = Employees.objects.create(**validated_data)
    #     for i in depts_data:
    #         Department.objects.create(dept_id=employee,**i)
    #     return employee

# class EmployeeSerializer(serializers.Serializer):
#     employee_id = serializers.IntegerField()
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     doj = serializers.DateTimeField()
#     dob = serializers.DateTimeField()
#     designation = serializers.CharField(max_length=25)
#     dept_id = serializers.()
#
#     def create(self, validated_data):
#         return Employees.objects.create(**validated_data)
#
#
#     def update(self, instance, validated_data):
#         instance.em = validated_data.get('dept_id', instance.dept_id)
#         instance.dept_name = validated_data.get('dept_name', instance.dept_name)
#         instance.manager = validated_data.get('manager', instance.manager)
#         instance.save()
#         return instance

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
