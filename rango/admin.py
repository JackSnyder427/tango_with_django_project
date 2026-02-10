from django.contrib import admin
from rango.PageAdmin import PageAdmin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
