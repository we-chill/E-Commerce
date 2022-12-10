from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [ProductInline]
    prepopulated_fields = {"slug": ("title",)}
