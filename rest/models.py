from django.db import models
from django.utils.timezone import now


class Score(models.Model):
    created_at = models.DateTimeField(editable=False, default=now, db_index=True)
    points_earned = models.PositiveIntegerField(default=0)
    points_possible = models.PositiveIntegerField(default=0)
    course_id = models.CharField(max_length=255, blank=False, db_index=True)
    user_id = models.CharField(max_length=255, blank=False, db_index=True)
    usage_id = models.CharField(max_length=255, blank=False, db_index=True)
    instance_id = models.CharField(max_length=255, blank=False, db_index=True, default='localhost')

    class Meta:
        ordering = ('created_at',)
