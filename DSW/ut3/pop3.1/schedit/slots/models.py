from django.db import models


class Slot(models.Model):
    start_at = models.TimeField(auto_now=True)
    end_at = models.TimeField(auto_now=True)

    def __str__(self):
        return f'{self.start_at.strftime("%I:%M")} - {self.end_at.strftime("%I:%M")}'

    class Meta:
        ordering = ['start_at', 'end_at']
        unique_together = ['start_at', 'end_at']
