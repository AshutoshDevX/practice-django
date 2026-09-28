from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to the blog home page!")

def about(request):
    a = 10+30
    return HttpResponse(f'About page: {a}')

def post_details(request,post_id):
    return HttpResponse(f'<h1>Show blog Post {post_id}</h1>')

def user_profile(request,username):
    return HttpResponse(f'<h1>Profile of User: {username} </h1>') 

def article_by_year(request, year):
    return HttpResponse(f'<h1>Articles from the year {year} </h1>')


def article_details(request, **kwargs):
    return HttpResponse(f'<h1>Articles from {kwargs['year']} - {kwargs['month']} </h1>')