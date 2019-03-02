from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import Context
from django.contrib.auth import(authenticate, get_user_model, login, logout) 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {
    }
    return render(request, "hoosuprightnow/index.html", context)

class SignUp(generic.CreateView):
    class SignUpForm(UserCreationForm):
        username = forms.CharField(max_length=10)
        email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

        class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2', )
    
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'hoosuprightnow/signup.html'


   
