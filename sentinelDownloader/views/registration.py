from django.contrib.auth.models import User


def create_superuser():
    username = 'admin'
    password = '123admin123'
    # email = ''

    if User.objects.filter(username=username).count() == 0:
        User.objects.create_superuser(username=username, password=password, email="entella@rambler.ru")  # email
        print('Superuser created.')
    else:
        print('Superuser creation skipped.')
    return
