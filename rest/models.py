from django.db import models


class TrackingLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    points_possible = models.IntegerField()
    points_earned = models.IntegerField()
    user_id = models.IntegerField()
    course_id = models.IntegerField()
    usage_id = models.IntegerField()
    instance_id = models.IntegerField()

    class Meta:
        ordering = ('created', )

