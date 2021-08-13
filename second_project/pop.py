import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')
import django
django.setup()

import random
from second_app.models import Userid
from faker import Faker

f = Faker()
def add_user(n):
    for i in range(n):
        fakename = f.name()
        fakeemail = f.email()
        user = Userid.objects.get_or_create(name = fakename,email = fakeemail )


if __name__ == '__main__':
    print('ok')
    add_user(20)
