from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

class BlogView(ListView): #html 템플릿 : 블로그 리스트를 담은 html 필요 : (소문자모델)_list.html
    model = ClassBlog

class BlogCreate(CreateView): # html: form(입력공간)을 갖고 있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView): # html: 상세 페이지를 담은 html : (소문자모델)_detail.html
    model = ClassBlog

class BlogUpdate(UpdateView): # html: form(입력공간)을 갖고 있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView): # html : "정말 지우시겠습니까?" : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')

    #template_model = 'classcrud/list.html >> 을 통해서 default 이름을 변경가능
    #context_object_name = 'blog_list' 를 통해서 object_list 가 아닌 것으로 사용가능, object가 사진첩인지, 블로그인지 모르니까


