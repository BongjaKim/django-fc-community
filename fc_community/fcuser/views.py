from django.shortcuts import render
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not (username and password):
            res_data['error'] = '모든 값을 입력하세요.'
        else:
            fcuser = Fcuser.objects.get(username=username)

            if check_password(password, fcuser.password):
                res_data['error'] = 'ok'
            else:
                res_data['error'] = '비밀번호가 틀립니다.'

        return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        useremail = request.POST.get('useremail', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif (password != re_password):
            res_data['error'] = '비밀번호가 틀립니다.'
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            fcuser.save()

        return render(request, 'register.html', res_data)
