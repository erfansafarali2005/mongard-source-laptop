from django.shortcuts import render , redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm , TodoUpdateForm

def home(request):

    all = Todo.objects.all()
    return render(request , 'home_app/home.html' , context={"todos" : all})

#def say_hello(request): # this function is caled via url
    #person = {'name' : 'amir'}
    #return render (request , "home_app/hello.html" , context=person) #template/ -> is added in setting directory
                                                                #   ^_> context is thing that will be sent into frontend

def detail(request , todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request , "home_app/detail.html" , context={'todo' :todo} )
    # in home template we type /detail/todo.id -> its wrong we use url_for instead


def delete(request , todo_id):
    try :
        Todo.objects.get(id = todo_id).delete() #delete method will delete that object
        messages.add_message(request , messages.SUCCESS , 'successfully deleted' , 'success')
    except:
        messages.error(request , 'there was an error' , 'danger')
    return redirect('home') #we only need to write url or name

def create(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST) #request.POST gather the information inside
        if form.is_valid(): #if everything was ok with authenticatiin and its called when submit botton is pressed
            cd = form.cleaned_data #cleaned data = data coming from the form
            Todo.objects.create(title = cd['form_title'] , body = cd['form_body'])
            messages.add_message(request , messages.SUCCESS , 'successfully created' , 'success')
            redirect('home')
        else:
            messages.add_message(request , messages.SUCCESS , 'an error accured' , 'success')

    else: #if request was get means he visited the url:
        form = TodoCreateForm()
    return render (request , "home_app/create.html" , context={"form" : form})



def update(request , todo_id):
    todo = Todo.obejcts.get(id = todo_id)

    if request.method == "POST":
        form = TodoUpdateForm(request.POST , instance = todo)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'successfully updated', 'success')
            return redirect('details' , todo_id)
    else:
        form = TodoUpdateForm()
    return render(request , 'home_app/update.html' , {'form' : form})