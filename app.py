#main.py
from flask import Flask, jsonify
app = Flask(__name__)
infos = [
    {
        "integrante": 1,
        "estado": "SP",
        "idade" : 26,
        "pet" : "true",
        "music": [
            {"name":"Chamego", "estilo": "MBP"}
        ]
    },
    {
        "integrante": 2,
        "estado": "RJ",
        "idade" : 40,
        "pet" : "false",
        "music": [
            {"name":"Coisa Linda", "estilo": "MBP"}
        ]
    },
    {
        "integrante": 4,
        "estado": "MG",
        "idade" : 52,
        "pet" : "true",
        "music": [
            {"name":"Aquarela", "estilo": "MBP"}
        ]
    }
]
@app.route('/')
def home():
    return jsonify(infos)

if __name__ == '__main__':
  app.run()