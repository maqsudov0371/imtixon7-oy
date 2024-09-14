from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'phone')
    list_filter = ('is_active',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'about_products', 'created_at', 'image', 'image1', 'image2', 'image3', 'image4')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(ForFooter)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("title", 'text', 'image', 'miniimage1', 'miniimage2', 'miniimage3', 'miniimage4', 'miniimage5')
    list_editable = ('text', 'image', 'miniimage1', 'miniimage2', 'miniimage3', 'miniimage4', 'miniimage5')
    list_display_links = ('title',)
