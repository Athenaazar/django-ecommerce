from django.db import models
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter', args={self.slug})


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:manufacturer_filter', args={self.slug})


class Product(models.Model):
    TAG_CHOICES = (
        ('', ''),
        ('out-of-stock', 'Hot'),
        ('new', 'New'),
        ('price-dec', 'Auction'),
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.CharField(max_length=300, choices=TAG_CHOICES, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='products')
    manufacturer = models.ForeignKey(Manufacturer, related_name='pmanufacturer', on_delete=models.CASCADE)
    short_descriptions = models.TextField()
    descriptions = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    discount_price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('updated',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product', args={self.slug})


class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)


class ProductFeatures(models.Model):
    product = models.ForeignKey(Product, default=None, related_name='features', on_delete=models.CASCADE)
    text = models.CharField(max_length=400)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)

    def __str__(self):
        return self.user.username


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
