from django.db import models

# Create your models here.


class board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    #models.TextField : 글자 길이가 제한이 없는 필드
    contents = models.TextField(verbose_name='내용')
    #user.User : user 앱의 User모델과 연결
    #on_delete : 해당 User 데이터가 삭제될경우 데이터 연관성 설정
    #models.CASCADE : 같이 삭제
    #models.SET_NULL : NULL값으로 게시글 변경
    #models.SET_DEFAULT : 지정된 디폴드 값으로 채운다.
    writer = models.ForeignKey('user.user',
                               on_delete=models.CASCADE,
                               verbose_name='작성자')
    registered_time = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록 시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'DOGE_board'
        verbose_name = 'DOGE게시물'
        verbose_name_plural = 'DOGE게시물'