from rest_framework import serializers

class AnalyticsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    month = serializers.CharField(max_length=20)