from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost
from django.shortcuts import redirect

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all() #모든 블로그 글들을 대상으로
    paginator = Paginator(blog_list, 3)#블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page')#request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    posts = paginator.get_page(page)#request된 페이지를 얻어온 뒤 return 해 준다
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) #위에 것들 다 처리한 다음에 redirect() 괄호 안의 유알엘로 넘기세요 // url은 항상 str형인데 blog.id는 int형이라서 str형으로 변환해줌 그래서 str씀

    ##redirect와 render의 차이는 뭐지? => 인자나 어떤 상황에 사용하고 싶은 경우에 따라서 달라짐 비슷하긴 한데 리다이렉트는 안에 유알엘을 받음 다른 유알엘을 입력할 수 있음 예를 들면 구글 사이트 근데 렌더는 뭐 인자로 파이썬 안에 있는거 인자로 받는데 뭔소린진 모르겠어

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> post
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    
    # 2. 빈페이지를 띄워주는 기능 -> get
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})