from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
fn = ''
gi = ''
pwd = ''
amt = ''
dat = ''


# Create your views here.


def sellaction(request):
    global fn, gi, pwd, amt, dat
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root",
                        passwd="abc123xyz$", database="web")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "full_name":
                fn = value
            if key == "giftcard_id":
                gi = value
            if key == "giftcard_password":
                pwd = value
            if key == "id_amount":
                amt = value
            if key == "expiry_date":
                dat = value

        c = "insert into user Values('{}','{}','{}','{}','{}')".format(
            fn, gi, pwd, amt, dat)
        cursor.execute(c)
        m.commit()
        return render(request, 'welcome.html')

    return render(request, 'sell_page.html')
