from rest_framework import serializers
from .models import Matl

class MatlSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Matl
		fields = ('id','name','url','price','company','qty')