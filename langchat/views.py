from django.shortcuts import render
from django.http import JsonResponse
from .chat_logic import get_answer





def index (request):
    return render(request, 'langchat/index.html')


def chat(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = get_answer(question)
        return JsonResponse({'answer': answer})
    return render(request, 'langchat/index.html')