from flask import Flask, request

app = Flask(__name__)

# Escolha seu VERIFY_TOKEN
VERIFY_TOKEN = "filhoDoHacher123"

@app.route("/", methods=["GET"])
def verify():
    token_sent = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token_sent == VERIFY_TOKEN:
        return str(challenge)
    return "Token inválido."

@app.route("/", methods=["POST"])
def receive_message():
    body = request.get_json()
    print("Mensagem recebida:", body)

    # Aqui no futuro você pode adicionar respostas automáticas
    return "Mensagem recebida", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
