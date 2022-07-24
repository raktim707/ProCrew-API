from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .import views

router = routers.DefaultRouter()
router.register('Inventory', views.InventoryViewSet)
router.register('Timetracker', views.TimeTrackerViewSet)
router.register('Task', views.TaskViewSet)
router.register('Crews', views.CrewsViewSet)
router.register('Picklist', views.PicklistViewSet)
router.register('Schedule', views.ScheduleViewSet)
router.register('Subscribers', views.SubscriberViewSet)
router.register('Employee', views.UserViewSet)
router.register('Attachments', views.AttachmentViewSet)
router.register('TimeOff', views.TimeOffViewSet)
router.register('TaskEmployees', views.TaskEmployeesViewSet)
urlpatterns = [
	path('', include(router.urls)),
]