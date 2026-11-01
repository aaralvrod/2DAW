from django.conf import settings
from django.db import models


class Appointment(models.Model):
    date = models.DateField()
    slot = models.ForeignKey(
        'slots.Slot',
        related_name='appointments',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='appointments', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.date.strftime("%Y-%m-%d")} ({self.slot})'

    class Meta:
        ordering = ['date', 'slot']
        unique_together = ['date', 'slot']
