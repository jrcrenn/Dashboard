from django.contrib import admin

from .models import Youtube_subs, Youtube_views, Youtube_popular
# Register your models here.

admin.site.register(Youtube_subs)
admin.site.register(Youtube_views)
admin.site.register(Youtube_popular)