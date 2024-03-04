from django.shortcuts import render
import requests
from django.http import JsonResponse
# from langchain.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI





def index (request):
    return render(request, 'langchat/index.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')

    # Chave da API da IA (substitua 'sua_chave_api_da_ia_aqui' pela sua chave de API válida)
    api_key = 'ls__b31bb9a08ffc4bb686298c5fbb4a4f20'

    # Endpoint da API da IA
    api_endpoint = 'https://api.smith.langchain.com'

    # Parâmetros da solicitação
    payload = {'message': userMessage, 'api_key': api_key}

    try:
        # Fazendo a solicitação para a API de IA
        response = requests.get(api_endpoint, params=payload)
        response_data = response.json()

        # Verificando se a solicitação foi bem-sucedida e obtendo a resposta da IA
        if response.status_code == 200 and 'response' in response_data:
            aiResponse = response_data['response']
            return JsonResponse({'response': aiResponse})
        else:
            return JsonResponse({'error': 'Resposta inválida da IA: ' + str(response_data)})
    except Exception as e:
        return JsonResponse({'error': 'Erro ao acessar a API da IA: ' + str(e)})