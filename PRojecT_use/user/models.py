from django.db import models

# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자 아이디')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    nick_name = models.CharField(max_length=32, verbose_name='닉네임')
    registered_time = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):  # Admin 페이지에 표시될 유저 이름 설정
        return self.username

    class Meta:
        db_table = 'DOGE_user'
        verbose_name = 'DOGE 사용자'  # 그룹 이름 변경
        verbose_name_plural = 'DOGE 사용자'  # 그룹이름 복수형 변경
