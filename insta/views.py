from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DocumentForm
from insta import models
from PIL import Image, ImageFilter
from insta.imagefilters import convert_grayscale, broken_glass


# just a little test function when things go awry
def world(request):
    HttpResponse('hello world. happy new year. peace on earth.')


# upload an image
def model_form_upload(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('insta:feed')
    return render(request, 'insta/add_pic.html', {'form': form})


# exaple of how to do it filters on view
def show_feed(request):
    pictures = [{
        'url': picture.photo.url.replace('insta/static', ''),
        'id': picture.id
    } for picture in models.DocumentForm.objects.all()][::-1]
    return render(request, 'insta/feed.html', {'pictures': pictures})


def grey_filter(request, image_id):
    path = models.DocumentForm.objects.get(id=image_id).photo.path
    convert_grayscale(path)
    models.DocumentForm.objects.get(id=image_id).save()
    return redirect('insta:feed')


def glass_filter(request, image_id):
    path = models.DocumentForm.objects.get(id=image_id).photo.path
    broken_glass(path)
    models.DocumentForm.objects.get(id=image_id).save()
    return redirect('insta:feed')
