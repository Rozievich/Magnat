from django.contrib import admin
from .models import Client, Media, Comment, Worker, MediaCategory

@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ['ism', 'tel_nomer', 'status', 'created_at']


@admin.register(Media)
class MediaModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']


@admin.register(Worker)
class WorkerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'familiya', 'sohasi']


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['ism', 'summary', 'status']

@admin.register(MediaCategory)
class MediaCargoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']