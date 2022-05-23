from django.shortcuts import redirect, render
from .models import board
from .forms import BoardForm
from user.models import user
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
# Create your views here.


def board_detail(request, pk):
    try:
        Board = board.objects.get(pk=pk)
    except board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board': Board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    if request.method == 'GET':
        form = BoardForm()
    elif request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            User = user.objects.get(pk=user_id)

            Board = board()
            Board.title = form.cleaned_data['title']
            Board.contents = form.cleaned_data['contents']
            Board.writer = User
            Board.save()

            return redirect('/board/list/')

    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    #order_by : 정렬 기준 이며 기본은 오름차순 - 는 내림차순
    boards = board.objects.all().order_by('-id')
    #p라는 이름으로 현재페이지를 받으며 2장 이상의 페이지가 안될경우 자동으로 1을 가져온다.
    page = int(request.GET.get('p', 1))  #p라는 이름으로 현재페이지를 받으며
    pagenator = Paginator(boards, 10)  #Pagenator 에 전체 개시물을 3개씩 페이징 시키는 코드

    boards = pagenator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})