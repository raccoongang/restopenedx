from rest_framework import serializers
from rest.models import Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ("id", "points_possible", "points_earned", "user_id", "course_id", "usage_id")
