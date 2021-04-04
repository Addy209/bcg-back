from rest_framework import serializers
from rest_framework import fields
from policy.models import Policy_tbl, Policy_feature

class PolicyTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Policy_tbl
        fields="__all__"

class PolicyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Policy_feature
        fields='__all__'
