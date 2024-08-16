from django.shortcuts import render
from blog.models import Post, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    
    # get all objects from Post models
    post_list = Post.objects.all()
    # make a pagination
    paginator = Paginator(post_list, 1) # retrieve a data and set a limit

    page = request.GET.get('page')
    # make a variable that returns a list_categories function in models.Category
    categories = Category.list_categories()

    try:
        posts = paginator.page(page)

    except PageNotAnInteger: #if page is not a number returns to first page
        posts = paginator.page(1)
    except EmptyPage: #if it is a empty page returns to last page
        posts = paginator.page(paginator.num_pages)

    # return a request to pages/home.html with posts and categories attributes
    return render(request, 'pages/home.html', {'posts': posts, 'categories': categories})

def single(request, single):

    # get id of post with single variable
    single = Post.objects.get(id=single)
    context = {
        'post': single 
    }
    return render(request, 'pages/single.html', context)

def archive(request, category):
    
    # get category objects with slug
    cat = Category.objects.get(slug=category)
    post_list = Post.objects.filter(category__pk=cat.id)
    paginator = Paginator(post_list, 1)

    page = request.GET.get('page')
    categories = Category.list_categories()

    try:
        posts = paginator.page('page')
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'pages/archive.html', {'posts': posts, 'categories' : categories, 'category': cat.title})

def imageDownload(request):
    allimages = Post.objects.all()
    return render(request, 'pages/show.html', {'images': allimages})
    print(allimages)