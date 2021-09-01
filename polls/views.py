from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, this is the index page")

def detail(request, question_id):
	return HttpResponse("question " % question_id)

def results(request, question_id):
	response = "result of question %s" 
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("voting on question %s." % question_id)
