from django.shortcuts import render, get_object_or_404
from .models import Question
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import QuestionForm, ChoiceForm


def question_add(request):
   if request.method == 'POST':
       form = QuestionForm(request.POST)

       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('polls:question_list'))

   else:
       form = QuestionForm()
       return render(request, 'polls/question_form.html', {'form': form})


def choice_add(request, question_id):
   if request.method == 'POST':
       data = request.POST
       form = ChoiceForm(data)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('polls:question_detail', kwargs={'question_id': question_id}))

   else:
       form = ChoiceForm(initial={'question': question_id})
       return render(request, 'polls/choice_form.html', {'form': form, 'question_id': question_id})


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'polls/question_list.html', {'questions': questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/question_detail.html', {'question': question})
