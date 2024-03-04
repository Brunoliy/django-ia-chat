import requests

def get_answer(question):
    url = "https://api.langgraph.com/answer"
    api_key = "ls__b31bb9a08ffc4bb686298c5fbb4a4f20"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"question": question}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get("answer")
    else:
        # Trate possíveis erros de comunicação com o serviço LangGraph
        return "Desculpe, não consegui encontrar uma resposta para essa pergunta."