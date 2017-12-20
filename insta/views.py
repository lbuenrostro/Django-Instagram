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
    pictures = models.DocumentForm.objects.all()
    return render(request, 'insta/feed.html', {'pictures': pictures})


# def upload_pic(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = ExampleModel.objects.get(pk=course_id)
#             m.model_pic = form.cleaned_data['image']
#             m.save()
#             return HttpResponse('image upload success')
#         else:
#             return (request, '/feed', {'form': form})
#     return HttpResponseForbidden('allowed only via POST')

# def upload_filters(request):
