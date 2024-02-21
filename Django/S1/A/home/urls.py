from django.urls import path
from . import views

urlpatterns=[ #this urls are called via main url in the main app
    path('' , views.home , name = 'home'), #emty path means nothing is written to write
    path('detail/<int:todo_id>' , views.detail , name = 'detail'), # now with name , even if we change the url , we don't loose the url path . it searchs for the url's name
    path('delete/<int:todo_id>' , views.delete , name = 'delete'),
    path('create/' , views.create , name = 'create'),
    path('update/<int:todo_id>' , views.update , name = 'update'),
]