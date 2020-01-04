from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product=product)
    form = ReviewForm
    session = request.session
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # логика для добавления отзыва
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.save()
            product_list = session.get('reviewed_products')
            if product_list:
                product_list.append(product.id)
                session['reviewed_products'] = product_list
            else:
                session['reviewed_products'] = [product.id]
            return redirect(product_list_view)

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
    }

    if session.get('reviewed_products') and product.id in session['reviewed_products']:
        is_review_exist = True
        context['is_review_exist'] = is_review_exist

    return render(request, template, context)
