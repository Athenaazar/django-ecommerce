from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ReviewForm
from .models import Category, Product, Manufacturer, Review, Wishlist
from django.urls import resolve
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from cart.forms import CartAddForm
from django.db.models import Q


def shop(request, slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False)
    manufacturer = Manufacturer.objects.all()
    if slug:
        url_name = resolve(request.path).url_name
        if url_name == 'category_filter':
            category = get_object_or_404(Category, slug=slug)
            products = products.filter(category=category)
        elif url_name == 'manufacturer_filter':
            manufacture = get_object_or_404(Manufacturer, slug=slug)
            products = products.filter(manufacturer=manufacture)
    paginator = Paginator(products, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    wishlisted_list = []
    if request.user.is_authenticated:
        wishlisted_list = list(
            Wishlist.objects.filter(user_id=request.user).values_list('product_id', flat=True).order_by('product_id'))
    form = CartAddForm()
    context = {
        'products': page_obj,
        'categories': categories,
        'manufacturer': manufacturer,
        'wishlisted_list': wishlisted_list,
        'form': form
    }

    return render(request, 'shop/shop.html', context)


def product_details(request, slug):
    form = CartAddForm()
    review_form = ReviewForm()
    review = Review.objects.filter(product__slug=slug)
    product = get_object_or_404(Product, slug=slug)
    if product:
        category_slug = [pr.slug for pr in product.category.all()]
        related_products = Product.objects.filter(available=True, category__slug__in=category_slug)
    wishlisted_list = []
    if request.user.is_authenticated:
        wishlisted_list = list(
            Wishlist.objects.filter(user_id=request.user).values_list('product_id', flat=True).order_by('product_id'))
    context = {
        'product': product,
        'review': review,
        'related_products': related_products,
        'wishlisted_list': wishlisted_list,
        'form': form,
        'review_form': review_form
    }
    return render(request, 'shop/product-details.html', context)


@login_required
@require_POST
def add_review(request, slug):
    form = ReviewForm(request.POST)
    product = get_object_or_404(Product, slug=slug)
    if form.is_valid():
        cd = form.cleaned_data
        review = Review(user=request.user, product=product, full_name=cd['full_name'], text=cd['text'])
        review.save()
        messages.success(request, 'thanks!', 'success')
    else:
        messages.success(request, 'please fill out the form correctly!', 'danger')
    return redirect('shop:product', slug)


@login_required
def liked(request):
    wishlist = {}
    if request.method == "GET":
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user_id=request.user.pk)
        else:
            print("Please login")
            return HttpResponse("login")

    return render(request, template_name='shop/wishlist.html', context={"wishlist": wishlist})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required
def add_to_wishlist(request):
    if is_ajax(request=request) and request.POST and 'attr_id' in request.POST:
        if request.user.is_authenticated:
            data = Wishlist.objects.filter(user_id=request.user.pk, product_id=int(request.POST['attr_id']))
            if data.exists():
                data.delete()
            else:
                Wishlist.objects.create(user_id=request.user.pk, product_id=int(request.POST['attr_id']))
    else:
        print("No Product is Found")

    return redirect("shop:shop")


def search(request):
    products = Product.objects.filter(available=True)
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(short_descriptions__icontains=query) | Q(descriptions__icontains=query))
        return render(request, 'shop/search.html', {'products': products,'query':query})
    else:
        return redirect("shop:shop")
