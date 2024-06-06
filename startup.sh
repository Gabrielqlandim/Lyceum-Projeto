set -e

source venv/Scripts/activate

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações do banco de dados
python manage.py migrate

# Iniciar o servidor
gunicorn --bind=0.0.0.0 --timeout 600 projeto.wsgi
