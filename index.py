"""
    Script de crear e iniciar de la aplicación
"""
# from decouple import config
from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
