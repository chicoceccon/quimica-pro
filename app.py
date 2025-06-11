from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🧪 Química Pro - Sistema Online!</h1>
    <p>Plataforma de resolução de questões de química com IA</p>
    <p>✅ Sistema funcionando perfeitamente!</p>
    <p>🚀 Em breve: Sistema completo</p>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
