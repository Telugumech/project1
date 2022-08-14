from django.views.generic import View, ListView,DetailView,CreateView,UpdateView,DeleteView
from exams.models import Marks
from django.urls import reverse_lazy
from django.shortcuts import render
   


# Create your views here.

def homepage(request):
    return render(request,'index.html')

def logoutUser(request):
    return render(request,'logout.html')

class Addmarks(CreateView):
    model = Marks
    fields = ('gfc','eng','wt1','bmee','ampp')

    
class marksRead(ListView):
    model = Marks


class Getmarks(DetailView):
    model = Marks
    


class Updatemarks(UpdateView):
    model = Marks
    fields = ('gfc','eng','wt1','bmee','ampp')


class Deletemarks(DeleteView):
    model = Marks
    success_url = reverse_lazy('listmarks')

