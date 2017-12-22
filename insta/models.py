from django.db import models


class DocumentForm(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='insta/static/insta/images')
