from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from utils.decorators import(
  require_http_methods,
  require_fields,
  allow_fields,
  check_unique_fields,
  cache_request
)

# Create your views here.
def index(request):
  return HttpResponse('Hello from app')


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

