from django.contrib import admin
from .models import Mijoz, PortfolioKategoriya, Portfolio, Blog, Hodim, Comment


@admin.register(Mijoz)
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


@admin.register(Portfolio)
class MediaModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']


@admin.register(Hodim)
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


@admin.register(PortfolioKategoriya)
class MediaCargoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary']