from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, get_object_or_404, redirect
from .models import Upload, Tag
from .forms import UploadForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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
    paginate_by = 4


class UserUploadListView(ListView):
    model = Upload
    template_name = 'Storage/user_uploads.html'
    context_object_name = 'uploads'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Upload.objects.filter(user=user).order_by('-date')


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


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, UploadForm):
            return str(obj)
        return super().default(obj)


def search_and_filter(request):
    error = ''
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data.get('tags')
            request.session['tags_passed'] = tags
            return redirect('Show_with_filters')
        else:
            error = 'Wrong form'
    form = UploadForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'Storage/search_and_filter.html', context)


class UploadWithFilters(ListView):
    template_name = 'Storage/home.html'
    context_object_name = 'uploads'
    ordering = ['-date']
    paginate_by = 4

    def get_queryset(self):
        tags_passed = self.request.session.get('tags_passed')
        filter_apply = Upload.objects.all()
        for tag in tags_passed:
            filter_apply = filter_apply.filter(tags__name=tag)
        return filter_apply

