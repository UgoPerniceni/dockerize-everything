from django.db import models
from django.conf import settings
from django.urls import reverse
from .choices import *

# Create your models here.
User = settings.AUTH_USER_MODEL

class Task(models.Model):
    author          = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title           = models.CharField(max_length = 120)
    description     = models.TextField(null=True, blank=True)
    creation_date   = models.DateTimeField()
    expected_end_date = models.DateTimeField(null=True, blank=True)
    complet_date    = models.DateTimeField(null=True, blank=True)
    status          = models.IntegerField(choices=STATUS_CHOICES, default=1)
    COLOR_CHOICES = (
        (0, 'Default'),
        (1, 'White'),
        (2, 'Blue'),
        (3, 'Red'),
        (4, 'Yellow')
    )
    color           = models.IntegerField(choices=COLOR_CHOICES, default=1)

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"id": self.id})