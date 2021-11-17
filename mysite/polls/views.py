from django.http import HttpResponse, response

def index(requests):
  return HttpResponse("Hello, world. You're at the polls index")

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results for question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s.", question_id)
