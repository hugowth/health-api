from django.db import models
from django.utils import timezone


class Organization(models.Model):
    name = models.TextField(
        unique=True,
        max_length=255,
    )
    create_date = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    update_date = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ['name']
