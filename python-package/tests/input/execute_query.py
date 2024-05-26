import sqlite3


def q(d, s):
    with sqlite3.connect(d) as c:
        x = c.cursor()
        x.execute(s)
        r = x.fetchall()
    return r
