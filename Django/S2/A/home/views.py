from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostUpdateForm
from django.utils.text import slugify

class HomeView(View):
    def get(self , request):
        posts = Post.objects.all()
        return render(request , 'home/index.html' , context={"posts" : posts})

class PostDetailView(View):
    def get(self , request , post_id , post_slug):
        #post = Post.objects.get(id=post_id , slug=post_slug)
        post = get_object_or_404(Post ,id=post_id, slug=post_slug) #if it returns DoesNotExit error it redirects the user to the 404 page
        return render(request , 'home/detail.html' , {'post' : post})

class PostDeleteView(LoginRequiredMixin , View):
    def get(self , request , post_id):
        post = get_object_or_404(Post , pk=post_id)
        #post = Post.objects.get(pk = post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request , 'post delete d sucesffully' , 'success')
        else:
            messages.danger(request , 'post could not be deleted' , 'danger')
        return redirect("home:home")

class PostUpdateView(LoginRequiredMixin , View):
    form_class = PostUpdateForm
    template_name = 'home/update.html'


    ### !!! now we use *args and **kwargs instead of directly getting the args from the request in methods , it looks better and has better performance !!!!###


    def setup(self, request, *args, **kwargs): #it saves the all data that we need to prevent looping through the database
        self.post_instance = get_object_or_404(Post , pk=kwargs['post_id'])
        #self.post_instance = Post.objects.get(pk=kwargs['post_id']) #is saved in self to be used on other methods
        return super().setup(request , *args , **kwargs)


    def dispatch(self , request , *args , **kwargs):
        #post = Post.objects.get(pk=kwargs['post_id']) #kwargs is a dictionary that contains args , post_id is located in there
        post = self.post_instance
        if not post.user.id == request.user.id: #if the owner of the post is no the owner of the request :
            messages.error(request , 'you cant update this post' , 'dnager')
            return redirect('home:home')
        return super().dispatch(request , *args , **kwargs)

    def get(self , request , *args , **kwargs):
        post_id =kwargs['post_id'] #here we can extract the post_Id from the **kwargs | we dont need it but for educational perposes
        #post = Post.objects.get(pk=post_id)
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request ,self.template_name , {'form' : form} )
        # if not post.user.id == request.user.id:
        #     messages.error(request , 'you cant update this post' , 'danger')
        #     return redirect('home:home')

    def post(self, request, *args , **kwargs):
        #post = Post.objects.get(pk=post_id)
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.save()
            messages.success(request, 'updates successfully', 'success')
            return redirect('home:post_detail', post.id, post.slug)
        #post = Post.objects.get(pk=post_id)
        # if not post.user.id == request.user.id:
        #     messages.error(request, 'you cant update this post', 'danger')
        #     return redirect('home:home')


class PostCreateView(LoginRequiredMixin , View):
    form_class = PostUpdateForm
    template_name = 'home/create.html'
    def get(self , request , *args , **kwargs):
        form = self.form_class
        return render(request , self.template_name , {'form' : form})
    def post(self , request , *args , **kwargs):
        form = self.form_class(request.POST) #request.post  : data coming from POST
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.user = request.user
            new_post.save()
            messages.success(request , 'you have successfully created  a new post' , 'success')
            return redirect('home:post_detail' , new_post.id , new_post.slug)

