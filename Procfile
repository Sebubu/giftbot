worker: python manage.py run_huey --workers 3 --worker-type process
web: gunicorn shopybot.wsgi --log-file - --timeout 1000