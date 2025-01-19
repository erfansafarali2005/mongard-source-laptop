from django.shortcuts import render , get_object_or_404 , redirect
from django.views import  View
from .models import Product , Category
from . import tasks
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from utils import IsAdminUserMixin
from orders.forms import CartAddForm

class HomeView(View):
    template_name = 'home/home.html'
    def get(self, request , category_slug=None): # None becasue maybe the user isnt lookign for category
        products = Product.objects.filter(available=True)
        #categories = Category.objects.all()
        categories = Category.objects.filter(is_sub = False)
        if category_slug: #if it wasn'n none
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category = category)
        return render(request, self.template_name , {'products':products ,
                                                        'categories' : categories
                                                     })

class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAddForm()
        return render(request , 'home/detail.html' , {'product':product , 'form':form})


class BucketHome(IsAdminUserMixin,View ):

    template_name = 'home/bucket.html'
    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request , self.template_name , {'objects':objects})

    # def test_func(self):
    # return self.request.user.is_authenticated and self.request.user.is_admin   -> we write it in utils to avoid repeating

class DeleteBucketObject(IsAdminUserMixin,View):
    def get(self, request, key):
        tasks.delete_bucket_objects_task.delay(key)
        messages.success(request , 'your object deleting' , 'info')
        return redirect('home:bucket')

    # def test_func(self):
    # return self.request.user.is_authenticated and self.request.user.is_admin   -> we write it in utils to avoid repeating

class DownloadBucketObject(IsAdminUserMixin,View):
    def get(self , request , key):
        tasks.download_object_task.delay(key)
        messages.success(request , 'your download begins' , 'info')
        return redirect('home:bucket')


    #def test_func(self):
        #return self.request.user.is_authenticated and self.request.user.is_admin   -> we write it in utils to avoid repeating