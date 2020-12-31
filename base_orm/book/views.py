from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
def index(request):
    # 添加一条数据
    book = Book(name='西游记',author='吴承恩',price=200)
    book.save()

    # 查询
    # 根据主键查找
    # primary_key
    # book = Book.objects.get(pk=3)
    # print(book)

    # 根据其他条件查找 (返回的是全部的，是列表）
    # books = Book.objects.filter(name='西游记')
    # books = Book.objects.filter(name='西游记').first()
    # print(books)

    # 删除数据
    # book = Book.objects.get(pk=1)
    # book.delete()

    # 修改数据
    # book = Book.objects.get(pk=3)
    # book.price = 150
    # book.save()
    return HttpResponse('图书添加成功！')