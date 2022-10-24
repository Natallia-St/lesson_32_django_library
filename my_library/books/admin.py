from django.contrib import admin
from .models import Authors, Categories, Books

admin.site.register(Authors)
admin.site.register(Categories)
admin.site.register(Books)
