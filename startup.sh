source venv/Scripts/activate

pip install -r requirements.txt

python manage.py migrate

gunicorn --bind=0.0.0.0 --timeout 600 projeto.wsgi