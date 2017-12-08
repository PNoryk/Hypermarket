from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product
from .forms import PostForm


# Create your views here.

def product_list(request):
    posts = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hypermarket/product_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Product, pk=pk)
    return render(request, 'hypermarket/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'hypermarket/post_edit.html', {'form': form})
