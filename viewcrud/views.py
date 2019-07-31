from django.shortcuts import render, redirect, get_object_or_404 #
from django.utils import timezone #
from .models import Blog #
from .forms import NewBlog #

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs':blogs})


def create(request):
    # 새로운 데이터 새로운 블로그 글을 저장하는 역할 == POST
    if request.method == 'POST':
        form = NewBlog(request.POST) 
        #어떤 형식의 입력공간으로 부터 받았고, 그 내용은 포스트에 담겨져있어
        if form.is_valid:
        #입력받은 값이 유효한 값인지 확인
            post = form.save(commit=False) #아직은 저장하지말고,
            post.pub_date = timezone.now() #현재 시간을 넣어서
            post.save() #저장해주세요!
        return redirect('home')

    # 글쓰기 페이지를 띄워주는 역할 == GET, POST가 아니었을 때, 
    else:
        form = NewBlog()
        return render(request, 'viewcrud/new.html',{'form':form})
    
    #즉, get방식이라면 새로운 페이지를 띄우고, 그페이지에서 post방식으로 전달, 저장

def update(request, pk):
    #어떤 블로그를 수정할 지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)
    #해당하는 블로그 객체의 pk에 맞는 입력공간을 가져오기
    form = NewBlog(request.POST, instance=blog)

    if form.is_valid():
        #입력받은 값이 유효한 값인지 확인
        form.save()
        return redirect('home')

    return render(request, 'viewcrud/new.html',{'form':form})



def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)#블로그모델에 해당하는 몇번째 데이터를, 블로그 변수에 담아주고
    blog.delete()
    return redirect('home')

