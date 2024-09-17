# Contenido de app.py:
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, mundo! Esta es una aplicación Flask desplegada en Vercel."

if __name__ == '__main__':
    app.run(debug=True)