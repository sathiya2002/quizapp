# quiz/views.py
from django.shortcuts import render, redirect
from .models import Question

def quiz(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})

def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        questions = Question.objects.all()
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer and user_answer == question.answer:
                score += 1
        return render(request, 'quiz/result.html', {'score': score, 'questions': questions})
    return redirect('quiz')


