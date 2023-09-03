# Import necessary Django modules
import os
import django
from django.contrib.auth.models import User

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro1.settings')
django.setup()

# Create a superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Huzaifa@1')
    print('Superuser created successfully!')
else:
    print('Superuser already exists.')
