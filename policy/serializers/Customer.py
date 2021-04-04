from rest_framework import serializers
from rest_framework import fields
from policy.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields = '__all__'