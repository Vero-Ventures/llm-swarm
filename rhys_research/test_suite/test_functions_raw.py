
# Calculate Fibonacci sequence
def f(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Merge two sorted lists
def m(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c

# Find the greatest common divisor using Euclid's algorithm
def g(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Find the maximum subarray sum (Kadane's Algorithm)
def k(l):
    m, c = float('-inf'), 0
    for n in l:
        c = max(n, c + n)
        m = max(m, c)
    return m

# Calculate factorial recursively
def f(n):
    return 1 if n == 0 else n * f(n - 1)





# Reading and processing a CSV file
import csv

def r(f):
    with open(f, mode='r') as c:
        r = csv.reader(c)
        h = next(r)
        d = [dict(zip(h, l)) for l in r]
    return d

# Connecting to a database and executing a query
import sqlite3

def q(d, s):
    with sqlite3.connect(d) as c:
        x = c.cursor()
        x.execute(s)
        r = x.fetchall()
    return r

# Sending an email using SMTP
import smtplib

def e(u, p, t, m):
    s = smtplib.SMTP('smtp.example.com', 587)
    s.starttls()
    s.login(u, p)
    s.sendmail(u, t, m)
    s.quit()

# Fetching JSON data from a web API
import requests

def j(u):
    r = requests.get(u)
    if r.status_code == 200:
        return r.json()
    else:
        return {}

# Performing a file search with regex
import os
import re

def s(p, r):
    m = re.compile(r)
    l = []
    for d, _, f in os.walk(p):
        for x in f:
            if m.search(x):
                l.append(os.path.join(d, x))
    return l
