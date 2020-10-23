import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactForm, ContactMessage, License, Post
from django.contrib import messages

from order.models import Order, ShopCart
from product.models import Category, Product, Images, Comment
from .forms import SearchForm




def index(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    lic = License.objects.all()
    post = Post.objects.all()
    products_slider = Product.objects.all().order_by('id')[:4]  #firs 4 products
    products_latest = Product.objects.all().order_by('-id')[:4] #last 4 product
    products_picked = Product.objects.all().order_by('?')[:4]   #Random selected 4 product

    page = "home"
    context = {
        'setting': setting,
        'page':page,
        'products_slider':products_slider,
        'products_latest': products_latest,
        'products_picked': products_picked,
        'category':category,
        'post':post,
        'lic':lic,


    }
    return render(request, 'index.html',context)

def aboutus(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    context = {
        'setting': setting,  'category':category,
    }
    return render(request, 'about.html', context)

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()#create relation with model
            data.name=form.cleaned_data['name']#get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()#save data to table
            messages.success(request, "Sizning xabaringiz yuborildi, xabaringiz uchun rahmat!")
            return HttpResponseRedirect('/contact/')

    setting = Setting.objects.all()
    form = ContactForm
    category = Category.objects.all()
    context = {
        'setting': setting, 'form': form, 'category':category,
    }
    return render(request, 'contact.html', context)

def category_products(request, id, slug):
    category=Category.objects.all()
    catdata =Category.objects.get(pk=id)
    products=Product.objects.filter(category_id=id)
    context = {
        'products':products,
        'category':category,
        'catdata':catdata,
    }
    return render(request, 'category_products.html', context)

def search(request):
    if request.method == 'POST': #Check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] #get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products = Product.objects.filter(title__icontains=query) #SELECT *FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {'products': products,
                       'query':query,
                       'category': category}
            return render(request, 'search.html', context)
    return HttpResponseRedirect('/')

def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    products = Product.objects.filter(title__icontains=q)
    results = []
    for rs in products:
      products_json = {}
      products_json = rs.title
      results.append(products_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)
def product_detail(request, id, slug):
    category=Category.objects.all()
    product=Product.objects.get(pk=id)
    images=Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {
        'product': product,
        'category': category,
        'images': images,
        'comments': comments,
    }
    return render(request, 'product_detail.html', context)


def post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post':post})


def lic(request):
    lic = License.objects.all()
    return render(request, 'lic.html', {'lic':lic})


def post_detail(request,id):
    category = Category.objects.all()
    product = Product.objects.all().order_by('?')[:8]
    post = Post.objects.get(pk=id)

    context = {
        'post': post,
        'category': category,
        'product':product,

    }
    return render(request, 'post_detail.html', context)

def lic_detail(request,id):
    category = Category.objects.all()
    product = Product.objects.all().order_by('?')[:8]
    lic = License.objects.get(pk=id)

    context = {
        'lic': lic,
        'category': category,
        'product':product,

    }
    return render(request, 'lic_detail.html', context)