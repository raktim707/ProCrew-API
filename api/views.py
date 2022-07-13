from rest_framework import generics, viewsets
from .models import Inventories
from .serializers import InventorySerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class InventoryViewSet(viewsets.ModelViewSet):
	"""
	list:	The inventory list action returns all available objects. It also accepts optional query parameters to filter inventory items.
	retrieve:	The inventory read action returns a single object selected by `id` 
	create:		The inventory create action expects the field name, metric, is_assembly, subscriber_id and creates a new object and returns it.
	update:		
	"""
	queryset = Inventories.objects.all()
	serializer_class = InventorySerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['category', 'metric', 'name']


class InventoryFilterList(generics.ListAPIView):
	serializer_class = InventorySerializer


