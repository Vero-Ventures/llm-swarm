import csv


def r(f):
    with open(f, mode="r") as c:
        r = csv.reader(c)
        h = next(r)
        d = [dict(zip(h, l)) for l in r]
    return d
