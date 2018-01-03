from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DocumentForm, FiltersForm
from insta import models
from PIL import Image, ImageFilter
from insta.imagefilters import convert_grayscale, broken_glass, rain_fall, fire_all
from django.views import View


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


# example of how to do it filters on view
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


def rain_filter(request, image_id):
    path = models.DocumentForm.objects.get(id=image_id).photo.path
    rain_fall(path)
    models.DocumentForm.objects.get(id=image_id).save()
    return redirect('insta:feed')


def fire_filter(request, image_id):
    path = models.DocumentForm.objects.get(id=image_id).photo.path
    fire_all(path)
    models.DocumentForm.objects.get(id=image_id).save()
    return redirect('insta:feed')


def remove(request, image_id):
    models.DocumentForm.objects.get(id=image_id).delete()
    return redirect('insta:feed')


class Apply_Filter(View):
    def get_pic(self, request, image_id):
        form = FiltersForm()
        path = 'insta/static/', models.DocumentForm.objects.get(
            id=image_id).image_url()
        return render(request, 'insta/feed.html', {'form': form})

    def post_pic(self, request, image_id):
        form = FiltersForm(request.POST)
        path = 'insta/static/' + models.DocumentForm.objects.get(
            id=image_id).image_url()
        image = Image.open(path)
        if form.is_valid():
            f = form.apply_filter()
            image.convert('RGB').Filter(f).save(path)
            return redirect('insta:feed')
        return render(request, 'insta/filter-image.html', {'form': form})
