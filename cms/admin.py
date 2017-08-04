from django.contrib import admin
from .models import Banner, BannerImage
# Register your models here.

class BannerImageInline(admin.TabularInline):
    model = BannerImage
    extra = 1
    readonly_fields = ('admin_thumb',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerImageInline]


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    pass