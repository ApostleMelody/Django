#encoding: utf-8

from django.shortcuts import render
from django.db import connection
def index(request):
    cursor = connection.cursor()
    # cursor.execute("insert into book(id,name,author) values(null,'三国演义','罗贯中')")
    result = cursor.execute("select * from book")
    # rows = cursor.fetchone()
    rows = cursor.fetchall()
    #rows = cursor.fetchman()
    for row in rows:
        print(row)
    return render(request,'index.html')