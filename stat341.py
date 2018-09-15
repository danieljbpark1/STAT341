from random import shuffle

def p_unmovable(s, n):
    C = s*n
    count = 0
    for i in range(1000000):
        deck = list(range(0,C))
        shuffle(deck)
        last4suits = deck[0:4]
        last4suits = [x // n for x in last4suits]
        if len(set(last4suits)) == 4:
            count += 1
    p = count / float(1000000)
    print(p)

p_unmovable(4,13)
