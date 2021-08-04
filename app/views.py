from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View

from .forms import RegisterAccountForm

from decorators import(
  require_http_methods,
  require_fields,
  allow_fields,
  check_unique_fields,
  cache_request
)

# Create your views here.
def index(request):
  return HttpResponse('Hello from app')

def home(request):
  return HttpResponse('welcome user')

def paginatePosts(qs, page):
    paginator = Paginator(qs, 12)

    try:
        posts = paginator.page(page)
    except:
        posts = []

    return {'list': posts, 'pg': paginator}

# static views
def static_template(templateName):
    def view(request):
        return render(request, templateName, {})
    return view

@cache_request('default_context', timeout=60*60*12)
def get_defualt_context(request=None):
    return {}


class register_account(View):
  def get(self, request, form=None):
    if request.user.is_authenticated:
      return redirect('/')

    context = { 'register_form': form or RegisterAccountForm }
    return render(request, 'register.html', context)


  def post(self, request):
    if request.user.is_authenticated:
      return redirect('/')

    form = RegisterAccountForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, 'Registration successful.' )
      return redirect('/')

    messages.error(request, 'Unsuccessful registration. Invalid information.')
    return self.get(request, form)


class login_account(View):
  def get(self, request, form=None):
    if request.user.is_authenticated:
      return redirect('/')

    context = { 'login_form': form or AuthenticationForm() }
    return render(request, 'login.html', context)

  def post(self, request):
    if request.user.is_authenticated:
      return redirect('/')

    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('/')

    messages.error(request,'Invalid username or password.')
    return self.get(request, form)


def logout_account(request):
  logout(request)
  messages.info(request, "You have successfully logged out.") 
  return redirect('/')
