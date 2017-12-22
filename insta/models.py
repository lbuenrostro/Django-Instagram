from django.db import models


class DocumentForm(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='insta/static/insta/images')
    filters = models.ImageField(upload_to='insta/static/insta/images')


# class PicturePost(models):
#     #Picture
#     picture = models.ImageField(upload_to='insta/static/insta/image')
#     def save (self,
