from django.contrib import admin
from .models import Serves,Serves_list,Texnologies,Developers
# Register your models here.

class PostImagesInline(admin.TabularInline):
    model = Serves_list
    extra = 1
class PostTexnologiesInline(admin.TabularInline):
    model = Texnologies
    extra = 1
class PostDevelopersInline(admin.TabularInline):
    model  = Developers
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostImagesInline,
        PostTexnologiesInline,
        PostDevelopersInline,
        ]

    readonly_fields = ()


admin.site.register(Serves,PostAdmin)
# admin.site.register(Serves_list)