from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse, Http404

from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
	try: 
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not Exist")
	return render(request, 'polls/detail.html', { 'question': question})

def results(request, question_id):
    # response = "You're looking at the results of question %s."
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', { 'question': question})

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)