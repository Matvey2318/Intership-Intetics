from django.http import HttpResponse, HttpRequest


class Authorization:
    """
    includes:
    - getting login and psswd
    - api
    """
    Login_data = dict()
    api = None

    def login(self, request):
        if 'login' in request.GET:
            self.Login_data['login'] = request.GET['login']
        else:
            return HttpResponse('No login in your form')
        if 'password' in request.GET:
            self.Login_data['password'] = request.GET['password']
            return
        else:
            return HttpResponse('No password in your form')