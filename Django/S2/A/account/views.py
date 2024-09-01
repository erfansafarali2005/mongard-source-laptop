from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from django.views import View
from .forms import UserRegisterationForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Post
class UserRegisterView(View): #now we use class , it must inherites from View

    form_class = UserRegisterationForm #form class is gharar dadi
    template_file = 'account/register.html'

    def dispatch(self, request, *args, **kwargs): #dispatch will be executed before get or post
        if request.user.is_authenticated:
            messages.error(request , 'you are alreaddy loggined , get back idiot !' , 'error')
            return redirect("home:home")     #now even if user uses the link , it dos't work
        return super().dispatch(request , *args , **kwargs) # returns the rest of the data with args and kwargs to get  post etc.
#                          ^-> we use dispatch again to return in to the dispatch again not other methods.
    def get(self , request): #if request.method == 'get'

        form = self.form_class() # class variable is saved as a class variable in self
        return render (request , self.template_file , context={'form' : form})

    def post(self , request): #if request.method == 'post'
        form = self.form_class(request.POST)
        if form.is_valid(): #now is_valid() also checks the clean_() function on my form
            cd = form.cleaned_data
            User.objects.create_user(username = cd['form_register_username'] , password = cd['form_register_password1'] , email = cd['form_register_email'])
            messages.success(request , 'you registered successfully' , 'success')
            return redirect("home:home")
        else : # if it was valdiate :
            messages.error(request, 'there was a problem in registseration please try again ', 'danger')
            return render (request , self.template_file , {'form' : form})
            # ^-> now if it was not valid , it dons't return debug error and it shows its validator error's   in form
        #its better to use try except


class UserLoginView(View):

    form_class = UserLoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: # if user was already loggined
            messages.error(request , 'you are alreaddy loggined , turn back idiot !' , 'error')
            return redirect("home:home")
        return super().dispatch(request , *args , **kwargs) #we return the rest of the built in code with its arguments to the next methods like get or post
    def get(self , request):
        form = self.form_class
        return render(request , self.template_name , context={'form' : form})


    def post(self , request):

        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username=cd['form_login_username'] , password=cd['form_login_password'])
            if user is not None: # if the user was filled with the user's data
                login(request , user)
                messages.success(request , 'you logged in successfully' , 'success')
                return redirect('home:home')
            else: #if it was empty
                messages.error(request , 'username or password is wrong' , 'danger')
        else:
            return render(request , self.template_name , context={'form' : form}) #this runs if user forgets its password to enter for instance


    # queries are lazy : in the code above user = athenticate , the query is not evaluated , its evaluated in the if statement

class UserLogoutView(LoginRequiredMixin,View): #when user enters the logout url , he can access to it but we dont want that
    # here we use LoginRequiredMixin instead of @login_required which is only used in fuction based views
    # !! if we had fuction based view , we could use @login_required decorator to limit the access of the loggined users
    #login_url = '/account/login' # its a gharar dadi variable that if user was loggined the LoginRequiredMixin it redirects the user to this url
    # ^ -> this can be set in settings.py too ! its better to set it in setting so we don't reapeat it on & on .
    def get(self , request):
        logout(request)
        messages.success(request , 'logged out successfully' , 'success' )
        return redirect(request , 'home:home')


class UserProfileView(View):
    template_name = 'account/profile.html'
    def get(self , request , user_id):
        user = get_object_or_404(Post , id=user_id)
        #user = User.objects.get(id = user_id) #pk = user_id   | for getting only one object
        posts = Post.objects.filter(user=user) #if it dosn't exist , it dosn't return error | for getting few objects
        #   we dont use get_list_or_404 becasue if the user wouldn't have any posts , it shows him 404 , but we dont need taht
        #                           ^-> user field in the model
        return render (request , self.template_name , {"user" : user , "posts" : posts})
    def post(self):
        pass