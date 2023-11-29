from django.contrib import admin
from .models import Client, Media, Comment, Worker, MediaCategory


@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ['ism', 'tel_nomer', 'status', 'sana']
    actions = ['kutishda', 'olmadi', 'rad_etilgan', 'qongiroq_qilingan']

    def kutishda(modeladmin, request, queryset):
        queryset.update(status=1)
    kutishda.short_description = "Kutishda"

    def olmadi(modeladmin, request, queryset):
        queryset.update(status=2)
    olmadi.short_description = "Olmadi"

    def rad_etilgan(modeladmin, request, queryset):
        queryset.update(status=3)
    rad_etilgan.short_description = "Rad etilgan"

    def qongiroq_qilingan(modeladmin, request, queryset):
        queryset.update(status=4)
    qongiroq_qilingan.short_description = "Qo'ng'iroq qilingan"


@admin.register(Media)
class MediaModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']


@admin.register(Worker)
class WorkerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'familiya', 'sohasi']


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['ism', 'summary', 'status']
    actions = ['approve_selected_comments', 'disapprove_selected_comments']

    def approve_selected_comments(modeladmin, request, queryset):
        queryset.update(status=True)
    approve_selected_comments.short_description = "Tanlangan commentlarni tasdiqlash"

    def disapprove_selected_comments(modeladmin, request, queryset):
        queryset.update(status=False)
    disapprove_selected_comments.short_description = "Tanlangan commentlarni rad etish"


@admin.register(MediaCategory)
class MediaCargoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']
