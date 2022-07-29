python3 manage.py makemigrations --no-input

python3 manage.py migrate --no-input

python3 manage.py collectstatic --no-input
python3 manage.py loaddata fixtures/admin.json

exec gunicorn config.wsgi:application -b 0.0.0.0:8000 --reload