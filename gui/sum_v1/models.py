from __future__ import unicode_literals

from django.db import models


class File_upload(models.Model):
    file = models.FileField(upload_to='sum_v1/upload', max_length = 500, blank = True)
    sum_words = models.IntegerField(default = 200, blank = True)

class SummaryRes(models.Model):
    doc = models.CharField(max_length = 200)
    summary = models.TextField()

    def __str__(self):
           return self.url
