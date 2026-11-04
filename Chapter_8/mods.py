def mods(a, n):
    r = a % n
    if r > n / 2:
        r -= n
    elif r <= -n / 2:
        r += n
    return r
