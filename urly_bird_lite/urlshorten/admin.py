from django.contrib import admin

# Register your models here.

from urlshorten.models import URL

admin.site.register(URL)