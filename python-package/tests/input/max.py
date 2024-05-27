def k(l):
    m, c = float("-inf"), 0
    for n in l:
        c = max(n, c + n)
        m = max(m, c)
    return m
