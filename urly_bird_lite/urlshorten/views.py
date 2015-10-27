from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View, CreateView, ListView, DetailView, TemplateView
from urlshorten.models import URL
# Create your views here.

class BaseView(TemplateView):
    template_name = "base.html"


class UrlCreateView(CreateView):
    model = URL
    fields = ["url", "author"]
    success_url = "/user"

    def form_valid(self, form):
        model = form.save(commit=False)
        model.author = self.request.user
        return super().form_valid(form)


class UrlListView(ListView):
    model = URL
    template_name = "urlshorten/url_view.html"


class UrlDetailView(DetailView):
    model = URL

