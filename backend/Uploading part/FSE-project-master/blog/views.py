from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })