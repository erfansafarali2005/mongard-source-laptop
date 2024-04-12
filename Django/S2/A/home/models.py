from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE) #get the user from the User model
    body = models.CharField(max_length=200)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True) #will be added with the date of the creation
    updated = models.DateTimeField(auto_now=True) #will be added on the date of the execution time (when user updates it )
    # !!!!!!!!!!! when you use auto_now or auto_add_now : you have no longer access to customize date it , it sets it automatically

    def __str__(self):
        return f'{self.slug} - {self.updated}'


    def get_absolute_url(self): #used when we want to use a link which is related to the data base
        return reverse("home:post_detail" , args=(self.id , self.slug)) #these two id and slugs are coming for url dynamic variable

        # when you use url in html , it also uses this reverse function


