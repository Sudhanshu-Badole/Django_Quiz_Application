import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Quiz
from django.utils import timezone

def update_quiz_status():
    now = datetime.now()
    Quiz.objects.filter(start_date__lte=now, end_date__gte=now).update(status='active')
    Quiz.objects.filter(end_date__lt=now).update(status='finished')


@csrf_exempt
def create_quiz(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question')
            options = data.get('options')
            right_answer = data.get('rightAnswer')
            start_date = data.get('startDate')
            end_date = data.get('endDate')

            if not question or not options or right_answer is None or not start_date or not end_date:
                return JsonResponse({'error': 'Missing required fields'})

            try:
                right_answer = int(right_answer)
            except ValueError:
                return JsonResponse({'error': 'Invalid value for rightAnswer'})

            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
                end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return JsonResponse({'error': 'Invalid date format'})

            # Create the quiz and set the initial status to 'inactive'
            quiz = Quiz.objects.create(
                question=question,
                options=options,
                right_answer=right_answer,
                start_date=start_date,
                end_date=end_date,
            )
            
            update_quiz_status()
            return JsonResponse({'quiz_id': quiz.id})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})
    return JsonResponse({'error': 'Invalid request method'})




def get_active_quiz(request):
    update_quiz_status()
    now = timezone.now()
    quizzes = Quiz.objects.filter(start_date__lte=now, end_date__gte=now, status='active')
    if quizzes:
        quiz_list = []
        for quiz in quizzes:
            quiz_data = {
                'question': quiz.question,
                'options': quiz.options,
                'status': quiz.status,
            }
            quiz_list.append(quiz_data)
        return JsonResponse({'quizzes': quiz_list})
    return JsonResponse({'error': 'No active quizzes found'})



def get_quiz_result(request, quiz_id):
    update_quiz_status()
    quiz = Quiz.objects.filter(id=quiz_id, status='finished').first()
    if quiz:
        return JsonResponse({
            'question': quiz.question,
            'right_answer': quiz.right_answer,
            'status': quiz.status,
        })
    return JsonResponse({'error': 'Quiz result not available'})

def get_all_quizzes(request):
    update_quiz_status()
    quizzes = Quiz.objects.all()
    print(quizzes)
    data = [{'question': quiz.question,
             'status': quiz.status,
             'quiz_id': quiz.id} for quiz in quizzes]
    return JsonResponse(data, safe=False)
