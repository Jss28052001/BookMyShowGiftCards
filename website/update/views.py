from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
em = ''
# Create your views here.


def updateaction(request):
    global em
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root",
                        passwd="abc123xyz$", database="web")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
        c = "insert into updates Values('{}')".format(em)
        cursor.execute(c)
        m.commit()

    return render(request, 'update_page.html')
