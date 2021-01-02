from rest_framework import serializers
from django.contrib.auth.models import User
from shortner.models import short_URL

class shortUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = short_URL
		fields = '__all__'