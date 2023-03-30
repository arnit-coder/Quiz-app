from django.shortcuts import render
from quiz.models import Question

def qpage(request):
	questions = Question.objects.all()

	return render(request, 'quiz.html', { 'questions': questions})
	
	
