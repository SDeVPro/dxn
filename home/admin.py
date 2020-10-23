from django.contrib import admin
from .models import Setting,  ContactMessage, Post, Images, License
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
class LicenseImageInline(admin.TabularInline):
    model = Images
    extra = 5

class LicenseAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    list_filter = ['title']
    readonly_fields = ('image_tag',)
    inlines = [LicenseImageInline]

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at']
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject','update_at']
    readonly_fields = ('name','subject', 'email', 'message','ip')
    list_filter = ['status']

admin.site.register(Post, PostAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Images)