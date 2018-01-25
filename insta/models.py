from django.db import models


class DocumentForm(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='insta/static/insta/images')

    def image_url(self):
        return self.photo.url[len('insta/images/'):]


class Comment(models.Model):
    comment = models.CharField(max_length=255, blank=True)
    document = models.ForeignKey(DocumentForm, on_delete=models.CASCADE)
