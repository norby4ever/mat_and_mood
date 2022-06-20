rts = ['хуй', 'хуе', 'хую', 'хуи', 'хуя', 'пизд', 'бля', 'ебан', 'ибан', 'муд', 'сук', 'суч', 'гонд', 'ганд', 'елд', 'пидо', 'педо', 'пида', 'педа', 'манд']
inp = open('russian.txt', 'r', encoding='cp1251')
c = 0
ignore = []
for i in inp.readlines():
    for j in rts:
        if j in i.strip():
            ignore.append(i)
    c += 1
    if c % 50000 == 0:
        print(c)
with open('ignorelist.json', 'w') as out:
    print('{\"ignorelist\": \"', end='', file=out)
    for i in ignore:
        print(i.strip(), end=', ', file=out)
    print('\"}', file=out)