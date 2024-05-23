import os, re


def s(p, r):
    m = re.compile(r)
    l = []
    for d, _, f in os.walk(p):
        for x in f:
            if m.search(x):
                l.append(os.path.join(d, x))
    return l
