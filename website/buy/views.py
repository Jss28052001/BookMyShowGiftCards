from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
am = ''
# Create your views here.


def buyaction(request):
    global am
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root",
                        passwd="abc123xyz$", database="web")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "amount":
                am = value
        c = "insert into buy1 Values('{}')".format(am)
        cursor.execute(c)
        m.commit()

    return render(request, 'buy_page.html')
