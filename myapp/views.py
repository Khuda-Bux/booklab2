from django.shortcuts import render
from .models import bloglab
from.forms import Mybloglab
from django .views.generic import CreateView,ListView,DetailView
# Create your views here.
#def bookhome(request):
    #book_data=bloglab.object.all()
    #return render(request, 'myapp/home.html',{'show',book_data})

class bookhome(ListView):
    model=bloglab
    fields=['title','updated_on','content','created_on','photo']
    template_name='myapp/home.html'

class bookdetail(DetailView):
    model=bloglab
    fields=['title','updated_on','content','created_on','photo']
    template_name='myapp/detail.html'
    success_url='/detail/'

class bookcreate(CreateView):
    model=bloglab
    fields=['title','content','photo']
    template_name= 'myapp/create.html'
    success_url='/create/'