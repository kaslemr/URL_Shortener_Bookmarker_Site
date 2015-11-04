from django.contrib import admin

# Register your models here.

from urlshorten.models import URL, ClickCount

admin.site.register(URL)
admin.site.register(ClickCount)