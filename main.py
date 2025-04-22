from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá! Eu sou o Filho do Hacher. 🤖🇧🇷"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
