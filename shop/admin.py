from django.contrib import admin
from .models import Product, Review, Category, ProductImages, ProductFeatures, Manufacturer


class ProductImagesInline(admin.StackedInline):
    model = ProductImages


class ProductFeaturesInline(admin.StackedInline):
    model = ProductFeatures


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImagesInline, ProductFeaturesInline]


@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_filter = ('name',)


@admin.register(Review)
class ReviewModel(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(Manufacturer)
class ManufacturerModel(admin.ModelAdmin):
    list_filter = ('name',)
