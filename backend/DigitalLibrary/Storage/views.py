from django.shortcuts import render
from .models import Upload
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'uploads': Upload.objects.all(),
    }
    return render(request, 'Storage/home.html', context)


class UploadListView(ListView):
    model = Upload
    template_name = 'Storage/home.html'
    context_object_name = 'uploads'
    ordering = ['-date']


class UploadDetailView(DetailView):
    model = Upload


class UploadCreateView(LoginRequiredMixin, CreateView):
    model = Upload
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UploadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Upload
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        upload = self.get_object()
        if self.request.user == upload.user:
            return True
        return False


class UploadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Upload
    success_url = '/'

    def test_func(self):
        upload = self.get_object()
        if self.request.user == upload.user:
            return True
        return False


def about(request):
    return render(request, 'Storage/about.html')
