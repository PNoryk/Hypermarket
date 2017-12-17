from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import PostForm


# Create your views here.

def request_str(request):
    r = request.__str__()
    return render(request, "hypermarket/product_list.html", {'req': r})


def product_list(request):
    posts = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "hypermarket/product_list.html", {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Product, pk=pk)
    return render(request, 'hypermarket/post_detail.html', {'post': post})


def post_new(request):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.picture = request.POST['picture']
            post.picture = request.POST['picture']
            print(form.cleaned_data)
            post.save()

            return redirect('post_detail', pk=post.pk)

        print(request.POST)
    else:
        form = PostForm()
    return render(request, 'hypermarket/post_edit.html', {'form': form})
