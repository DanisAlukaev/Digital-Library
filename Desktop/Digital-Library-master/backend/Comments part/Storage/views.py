from django.shortcuts import render, get_object_or_404, redirect
from .models import Upload, Comment
from .forms import UploadForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from datetime import date

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
        'comment_form': CommentForm,
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            content_connected=self.get_object()).order_by('date_posted')
        data['comments'] = comments_connected
        data['comment_form'] = CommentForm()
        print(str(data['comment_form']))

        return data

    def post(self, request, *args, **kwargs):
        if request.POST.get('content') is None:
            pass # TODO: error
        new_comment = Comment(content=request.POST.get('content'),
                              author=self.request.user,
                              content_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class UploadCreateView(LoginRequiredMixin, CreateView):
    model = Upload
    fields = ['title', 'content', 'document', 'tags']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UploadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Upload
    fields = ['title', 'content', 'document', 'tags']

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


def search_and_filter(request):
    error = ''
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            search_for = form.cleaned_data.get('search_for')
            tags_passed = form.cleaned_data.get('tags_passed')
            date_passed = form.cleaned_data.get('date_passed')
            request.session['search_for'] = search_for
            request.session['tags_passed'] = tags_passed
            if date_passed is None:
                request.session['date_passed'] = date_passed
            else:
                request.session['date_passed'] = date_passed.isoformat()
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
        search_for = self.request.session.get('search_for')
        tags_passed = self.request.session.get('tags_passed')
        if self.request.session.get('date_passed') is None:
            date_passed = None
        else:
            date_passed = date.fromisoformat(self.request.session.get('date_passed'))

        filter_apply = Upload.objects.all()

        filter_apply = filter_apply.filter(title__icontains=search_for)
        for tag in tags_passed:
            filter_apply = filter_apply.filter(tags__name=tag)
        if date_passed is not None:
            filter_apply = filter_apply.filter(date__date=date_passed)
        return filter_apply
