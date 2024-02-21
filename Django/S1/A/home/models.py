from django.db import models

# dont forget to run >>python manage.py makemigrations and >>pythpn manage.py migrate , after creating your model
# in migrations directory there is a initial file which is the setting of your database , dont edit it !

class Todo(models.Model): #everymodel should inherites from models.Model
    #different field are stored in models method
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=50)


    def __str__(self): # if any object is represented , it shows its title now
        return self.title