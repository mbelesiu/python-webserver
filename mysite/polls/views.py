from django.http import HttpResponse

def index(requests):
  return HttpResponse("Hello, world. You're at the polls index")
