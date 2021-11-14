from django.shortcuts import render
from django.http import HttpRequest

def index(requests):
  return HttpRequest("Hello, world. You're at the pills index")
