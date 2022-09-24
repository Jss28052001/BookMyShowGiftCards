from django.shortcuts import render
from sqlite3 import Cursor
import mysql.connector as sql
em = ''
pwd = ''
# Create your views here.


def loginaction(request):
    global em, pwd
    if request.method == 'POST':
        m = sql.connect(host='localhost', user='root',
                        passwd='abc123xyz$', database='web')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        c = "select * from users2 where email='{}' and password='{}'".format(
            em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            return render(request, 'welcome.html')

    return render(request, 'login_page.html')
