from django.db import models


class DocumentForm(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='insta/static/insta/images')
    # image = models.ImageField(upload_to='insta/static/insta/images')
    # uploaded_at = models.DateTimeField(auto_now_add=True)


# class ExampleModel(models.Model):
#     model_pic = models.ImageField(
#         upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
