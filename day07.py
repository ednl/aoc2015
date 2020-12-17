import re
regrule = re.compile(r'^(([a-z0-9]+) )?(([A-Z]+) )?([a-z0-9]+) -> ([a-z]+)\n$')

fun = {
    'AND'   : lambda x, y: x & y,
    'OR'    : lambda x, y: x | y,
    'NOT'   : lambda x: ~x,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y,
    'PATCH' : lambda x: x}

h = {}
with open('input07.txt') as f:
    for line in f:
        m = regrule.match(line)
        if m:
            f = fun[m.group(4) if m.group(4) is not None else 'PATCH']
            u = [int(x) if x.isnumeric() else x for x in m.group(2, 5) if x is not None]
            y = m.group(6)
            h[y] = {'f': f, 'u': u}

def getval(id):
    if type(id) is int:
        return id
    if id in val:
        return val[id]
    inp = list(map(getval, h[id]['u']))
    for u, v in zip(h[id]['u'], inp):
        val[u] = v
    return h[id]['f'](*inp)

# Part 1
val = {}
print(getval('a'))

# Part 2
val = {'b': 46065}
print(getval('a'))
