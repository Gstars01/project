from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import user
from django.contrib.auth.hashers import make_password,check_password
from .forms import LoginForm


# Create your views here.


def register(request):  # request: 사용자가 서버(회사) 에 요청할 데이터가 들어있는 객체
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        email = request.POST.get('email')
        nick_name = request.POST.get('nick_name')
        res_data = {}
        if not (username and password and re_password and email and nick_name):
            res_data['error'] = '모든 정보를 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            NewUser = user(username=username, password=make_password(
                password), email=email, nick_name=nick_name)
            NewUser.save()
    return render(request, 'home.html', res_data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        Username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (Username and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        else:
            CurUser = user.objects.get(username=Username)
            if check_password(password, CurUser.password):
                request.session['user'] = CurUser.id  # 서버에 세션 등록 과정
                return redirect('/')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
        return render(request, 'login.html', res_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def home(request):
    User_id = request.session.get('user')
    if User_id:
        UserData = user.objects.get(pk=user.id)
        return HttpResponse(UserData.username)
    return render(request, 'home.html')
