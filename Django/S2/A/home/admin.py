from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): #new class to edit the admin panel
    list_display = ('user' , 'slug' , 'updated') #collumns of the models page
    search_fields = ('slug',) #the searchfield
    list_filter = ("updated",) #filter of the admin
    prepopulated_fields = {'slug' : ('body',)} #this automatically fills the slug while creading the opject
    raw_id_fields = ('user',) #now the id field is advanced with the search option instead of drop down menu

# the decorator with the Post method is working on the PostAdmin class instead of admin.site.register(Post , PostAdmin)