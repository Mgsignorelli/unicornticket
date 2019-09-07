web: python manage.py collectstatic --noinput; gunicorn UnicornTicketSystem.wsgi:application
release: python manage.py migrate
