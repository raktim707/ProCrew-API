from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Inventories, TimeTrackers, Tasks, Picklists, Schedules, Subscribers, Users, Crews, Attachments, TimeOff, TaskEmployees
from .serializers import InventorySerializer, TimeTrackerSerializer, TaskSerializer, PicklistSerializer, ScheduleSerializer, SubscriberSerializer, UserSerializer, CrewSerializer, AttachmentSerializer, TimeOffSerializer, TaskEmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class InventoryViewSet(viewsets.ModelViewSet):
	"""
	list:	The inventory list action returns all available objects. It also accepts optional query parameters to filter inventory items. By default, if you do not pass any query parameters, it will return the list of all objects.
	retrieve:	The inventory read action returns a single object selected by `id` 
	create:		The inventory create action expects the field name, metric, is_assembly, subscriber_id and creates a new object and returns it.
	update:		The inventory update action updates an object selected by `id`
	"""
	queryset = Inventories.objects.all()
	serializer_class = InventorySerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['category', 'metric', 'name']

class TimeTrackerViewSet(viewsets.ModelViewSet):

	queryset = TimeTrackers.objects.all()
	serializer_class = TimeTrackerSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['user', 'start', 'end', 'break_field', 'status', 'approved_by', 'approval_date']


class TaskViewSet(viewsets.ModelViewSet):
	queryset = Tasks.objects.all()
	serializer_class = TaskSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['schedule', 'start', 'status', 'crew']

class PicklistViewSet(viewsets.ModelViewSet):
	queryset = Picklists.objects.all()
	serializer_class = PicklistSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['subscriber', 'schedule', 'task', 'name']

class SubscriberViewSet(viewsets.ModelViewSet):
	queryset = Subscribers.objects.all()
	serializer_class = SubscriberSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['company_name', 'mobile_number', 'wc_subscription_id', 'customer_id', 'status', 'num_users_availed', 'timezone']

class ScheduleViewSet(viewsets.ModelViewSet):
	queryset = Schedules.objects.all()
	serializer_class = ScheduleSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['subscriber', 'builder', 'subdivision', 'contact_name', 'model', 'permit_number', 'archive', 'is_schedule']


class UserViewSet(viewsets.ModelViewSet):
	"""
	list:	The Employee list action returns all available user instances who has an **employee_no**. It also accepts the following optional query parameters to filter employee instances. By default, if you do not pass any query parameters, it will return the list of all objects.
	retrieve:	The employee read action returns a single object selected by `id` 
	create:		The employee create action expects the following fields below in payload and creates a new object and returns it.
	update:		The employee update action updates an object selected by `id`
	delete:		The employee delete action deletes an object selected by `id`
	"""
	queryset = Users.objects.exclude(employee_no__isnull=True)
	serializer_class = UserSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['employee_no', 'subscriber', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'last_raise', 'pay_rate', 'address', 'termination', 'archive']
	

'''class ListEmployees(APIView):
	serializer_class = UserSerializer
	def get(self, request, format=None):
		employees = Users.objects.exclude(employee_no__isnull=True)
		serializer = UserSerializer(employees, many=True)
		return Response(serializer.data, status=status.HTTP_200_ok)'''



class CrewsViewSet(viewsets.ModelViewSet):
	"""
	list:	The crews list action returns all available crew instances. It also accepts the following optional query parameters to filter crew instances. By default, if you do not pass any query parameters, it will return the list of all objects.
	retrieve:	The crews read action returns a single object selected by `id` 
	create:		The crews create action expects the required field `name`, `is_archive`, `is_manual`,`subscriber_id` in payload and creates a new object and returns it.
	update:		The crews update action updates an object selected by `id`
	delete:		The crews delete action deletes an object selected by `id`
	"""
	queryset = Crews.objects.all()
	serializer_class = CrewSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['subscriber', 'name', 'description', 'created_at', 'updated_at', 'color', 'is_archive', 'is_manual']



class AttachmentViewSet(viewsets.ModelViewSet):
	"""
	list:	The Attachmets list action returns all available attachment instances. It also accepts the following optional query parameters to filter attachment instances. By default, if you do not pass any query parameters, it will return the list of all objects.
	retrieve:	The Attachmets read action returns a single object selected by `id` 
	create:		The Attachmets create action expects the required field `file_path` and `schedule` in payload and creates a new object and returns it.
	update:		The Attachmets update action updates an object selected by `id`
	delete:		The Attachmets delete action deletes an object selected by `id`
	"""
	queryset = Attachments.objects.all()
	serializer_class = AttachmentSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['schedule', 'filename', 'created_at', 'updated_at', 'filepath']


class TimeOffViewSet(viewsets.ModelViewSet):
	queryset = TimeOff.objects.all()
	serializer_class = TimeOffSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['user_id', 'subscriber_id', 'start_date', 'end_date', 'all_day', 'reason', 'status', 'processed_by', 'is_archive']

class TaskEmployeesViewSet(viewsets.ModelViewSet):
	"""
	list:	The TaskEmployee list action returns all available TaskEmployee instances with the details of task instance assigned to employees. It also accepts the following optional query parameters to filter TaskEmployee instances. By default, if you do not pass any query parameters, it will return the list of all objects.
	retrieve:	The TaskEmployee read action returns a single object selected by `id` 
	create:		The TaskEmployee create action expects the required field `employee_id`, `role`, `task` in payload and creates a new object and returns it.
	update:		The TaskEmployee update action updates an object selected by `id`
	delete:		The TaskEmployee delete action deletes an object selected by `id`
	"""
	queryset = TaskEmployees.objects.all()
	serializer_class = TaskEmployeeSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['employee_id', 'role', 'crew_id', 'task']