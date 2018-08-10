# from django.shortcuts import render, redirect

# # from .forms import RegisterForm
# from carservice.forms import *
# from carservice.models import *
# from django.contrib import messages
# from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import TypeNewsForm
from carservice.models import TypeNews
from django.contrib import messages

# from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView




class TypeNewsList(ListView):
    template_name = 'carservice/typenews/index.html'
    model  = TypeNews

class TypeNewsDetail(DetailView):
    template_name = 'carservice/typenews/show.html'
    model  = TypeNews

class TypeNewsCreate(CreateView):
    template_name = 'carservice/typenews/form.html'
    model = TypeNews
    form_class = TypeNewsForm
    success_url = '/admin/typenews'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class TypeNewsUpdate(UpdateView):
    template_name = 'carservice/typenews/form.html'
    form_class = TypeNewsForm
    model = TypeNews
    success_url = '/admin/typenews'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class TypeNewsDelete(DeleteView):
    model = TypeNews
    success_url = '/admin/typenews'
    
        
