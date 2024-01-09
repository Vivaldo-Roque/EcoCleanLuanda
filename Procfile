web: daphne EcoCleanLuanda.asgi:application -u /tmp/daphne.sock -p 80 -b 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2