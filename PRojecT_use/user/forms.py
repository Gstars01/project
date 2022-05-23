from django import forms
from .models import user
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):  # 장고에서 제공하는 field 태그 사용하기
    username = forms.CharField(error_messages={'required': '아이디를 입력해주세요.'},
                               max_length=32,
                               label="사용자 이름")
    password = forms.CharField(error_messages={'required': '비밀번호를 입력해주세요.'},
                               widget=forms.PasswordInput,
                               label="비밀번호")

    def clean(self):  # 로그인 요청시 넘어오는 메소드
        cleaned_data = super().clean()  # 부모Class 의 Clean 데이터(사용자 데이터) # 아이디 들고오기'
        userName = cleaned_data.get('username') 
        password = cleaned_data.get('password')  # 비밀번호 들고오기
        if userName and password:  # 아이디 비밀번호가 입력되어있는지 체크
            try:
                # 입력된 아이디로 Database에 등록된 아이디 들고오기
                print(userName)
                CurUser = user.objects.get(username=userName)
            except user.DoesNotExist:  # 존재하는 아이디인지 체크
                self.add_error('username', '아이디가 없습니다.')
                return

            if not check_password(password, CurUser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else:
                self.user_id = CurUser.id
