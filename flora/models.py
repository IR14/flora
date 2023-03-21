import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin


class Feedback(models.Model):
    user = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    feedback_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.feedback_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
