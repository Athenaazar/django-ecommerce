from django.contrib import admin
from .models import Product, Review, Category, ProductImages


class ProductImagesInline(admin.StackedInline):
    model = ProductImages


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImagesInline]


@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_filter = ('name',)
