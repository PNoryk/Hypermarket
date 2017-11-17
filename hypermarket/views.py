from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Product
from .forms import PostForm
# Create your views here.


def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hypermarket/product_list.html', {'posts': products})


def post_detail(request, pk):
    post = get_object_or_404(Product, pk=pk)
    return render(request, 'hypermarket/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'hypermarket/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'hypermarket/post_edit.html', {'form': form})