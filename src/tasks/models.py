from django.db import models
from django.conf import settings
from django.urls import reverse
import datetime
# from .choices import *

# Create your models here.
User = settings.AUTH_USER_MODEL

class Task(models.Model):
    author          = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title           = models.CharField(max_length = 120)
    description     = models.TextField(null=True, blank=True)
    creation_date   = models.DateTimeField()
    # expected_end_date = models.DateTimeField(null=True, blank=True)
    complet_date    = models.DateTimeField(null=True, blank=True)
    STATUS_CHOICES = (
        (1, ("Active")),
        (2, ("Done"))
    )
    status          = models.IntegerField(choices=STATUS_CHOICES, default=1)
    COLOR_CHOICES = (
        (1, 'Default'), #White
        (2, 'Light'), #Light
        (3, 'Turquoise'), #Info
        (4, 'Orange'), #Warning
        (5, 'Red'), #Danger
        (6, 'Green'), #Success
        (7, 'Blue'), #Primary
    )
    color           = models.IntegerField(choices=COLOR_CHOICES, default=1)

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"id": self.id})

    def close(self):
        if self.status == 1:
            self.status = 2
            self.complet_date = datetime.datetime.now()