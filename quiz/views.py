from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Result
from django.contrib.auth.decorators import login_required

def home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/home.html', {'quizzes': quizzes})


@login_required
def quiz_page(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    
    if request.method == 'POST':
        score = 0
        for q in questions:
            answer = request.POST.get(str(q.id))
            if answer and int(answer) == q.correct_option:
                score += 1
        Result.objects.create(user=request.user, quiz=quiz, score=score)
        return render(request, 'quiz/result.html', {'score': score, 'quiz': quiz})
    
    return render(request, 'quiz/quiz_page.html', {'quiz': quiz, 'questions': questions})


@login_required
def result_page(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    result = Result.objects.filter(user=request.user, quiz=quiz).first()
    return render(request, 'quiz/result.html', {'quiz': quiz, 'result': result})
