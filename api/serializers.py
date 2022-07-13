from rest_framework import serializers
from .models import *


class InventoryPicklistSerializer(serializers.ModelSerializer):
	class Meta:
		model = InventoryPicklists
		fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
	#inventorypicklists = InventoryPicklistSerializer(many=True, read_only=True, source='inventorypicklists_set')
	class Meta:
		model = Inventories
		fields = ['id', 'parent', 'created_at', 'updated_at', 'deleted_at', 'category', 'user', 'metric', 'name', 'description', 'is_assembly', 'subscriber_id', 'main_image_id', 'low_inventory_warning']
