from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View, CreateView, ListView, DetailView, TemplateView
from urlshorten.models import URL
from hashlib import md5
import hashlib
# Create your views here.

class BaseView(TemplateView):
    template_name = "base.html"


class UrlCreateView(CreateView):
    model = URL
    fields = ["url", "author", "description"]
    success_url = "/user"

    def form_valid(self, form):
        model = form.save(commit=False)
        model.author = self.request.user
        _url = bytes(form.instance.url, 'utf8')
        m = md5(_url)
        _shortened_url = m.hexdigest()
        form.instance.shortened_url = "hpz" + _shortened_url[:7]
        model.shortened_url = form.instance.shortened_url
        return super().form_valid(form)

#class UrlShortView(View):


class UrlListView(ListView):
    model = URL
    template_name = "urlshorten/url_view.html"

    class Meta:
        ordering = ('-datetime')


class UrlUserList(ListView):
    model = URL
    template_name = "urlshorten/url_list.html"

    def get_queryset(self):
        user = self.kwargs.get('pk')
        return self.model.objects.filter(author__id=user)

class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/accounts/profilelogin"





