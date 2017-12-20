from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DocumentForm
from insta import models

# from .forms import UploadFileForm


def world(request):
    HttpResponse('world')


def model_form_upload(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('insta:feed')
    else:
        return render(request, 'insta/add_pic.html', {'form': form})


def show_feed(request):
    # data = models.DocumentForm.objects.all()
    # pictures = []
    # for picture in data:
    #     pictures.append(picture.photo.url.replace('insta/static', ''))
    pictures = [
        picture.photo.url.replace('insta/static', '')
        for picture in models.DocumentForm.objects.all()
    ]
    return render(request, 'insta/feed.html', {'pictures': pictures})
