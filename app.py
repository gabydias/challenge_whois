#main.py
from flask import Flask, jsonify
app = Flask(__name__)
infos = [
    {
        "id": "1",
        "music": [
            {"name":"Coisa Linda", "estilo": "MBP"}
        ], 
        "estado": "SP",
        "filme": [
            {"name":"Premonição", "estilo": "Terror"}
        ], 
    },
    {
        "id": "2",
        "music": [
            {"name":"Aquarela", "estilo": "MBP"}
        ], 
        "estado": "RJ",
        "filme": [
            {"name":"Fragmentado", "estilo": "Suspense"}
        ], 
    }
]
@app.route('/')
def infos():
    return jsonify(infos)

if __name__ == '__main__':
  app.run()