from rest_framework import serializers
from .models import *
from django.http import JsonResponse


class InventoryPicklistSerializer(serializers.ModelSerializer):
	class Meta:
		model = InventoryPicklists
		fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
	#inventorypicklists = InventoryPicklistSerializer(many=True, read_only=True, source='inventorypicklists_set')
	class Meta:
		model = Inventories
		fields = ['id', 'parent', 'created_at', 'updated_at', 'deleted_at', 'category', 'user', 'metric', 'name', 'description', 'is_assembly', 'subscriber_id', 'main_image_id', 'low_inventory_warning']

class TimeTrackerSerializer(serializers.ModelSerializer):
	class Meta:
		model = TimeTrackers
		fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tasks
		fields = '__all__'

class PicklistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Picklists
		fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schedules
		fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscribers
		fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Crews
		fields = ['__all__']

class CrewEmployeesField(serializers.RelatedField):
	def to_representation(self, value):
		new_val = {'Crew ID' : value.crew.id, 'Crew Name': value.crew.name}
		return new_val
	'''class Meta:
					model = CrewEmployees
					fields = ['crew']'''



class UserSerializer(serializers.ModelSerializer):
	crewemployees = CrewEmployeesField(many=True, read_only=True)
	class Meta:
		model = Users
		fields = ['id', 'employee_no', 'username', 'email', 'first_name', 'middle_name','last_name', 'mobile_number', 'phone_number', 'address', 'pay_rate', 'last_raise', 'termination', 'archive', 'site_wide', 'start_date','crewemployees']

class CrewSerializer(serializers.ModelSerializer):
	tasks = TaskSerializer(many=True, read_only=True)
	class Meta:
		model = Crews
		fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Attachments
		fields = '__all__'

class TimeOffSerializer(serializers.ModelSerializer):
	class Meta:
		model = TimeOff
		fields = '__all__'


class TaskEmployeeSerializer(serializers.ModelSerializer):

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['task'] = TaskSerializer(instance.task).data
		return response
	class Meta:
		model = TaskEmployees
		fields ='__all__'