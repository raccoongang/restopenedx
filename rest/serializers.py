from rest_framework import serializers
from rest.models import TrackingLog

class TrackingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingLog
        fields = ("id", "points_possible", "points_earned", "user_id", "course_id", "usage_id", "instance_id")
