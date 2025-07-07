import requests

def consultar_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except requests.RequestException as e:
        print(f"Falha na requisição: {e}")
        return

    usuarios = resposta.json()
    for u in usuarios:
        print(f"ID: {u['id']} – {u['name']} – {u['email']}")

if __name__ == "__main__":
    consultar_usuarios()
