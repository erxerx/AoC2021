def win(bn):
    global seen
    for q in range(5):
        rc = cc = 0
        for w in range(5):
            if int(bb[bn][q][w]) in seen:
                rc += 1
            if int(bb[bn][w][q]) in seen:
                cc += 1
        if rc == 5 or cc == 5:
            return True
    return False


with open('d04.in', 'r') as f:
    content = f.read()
c = content.split('\n\n')
bb = []
for i in range(100):
    bb.append([x.split(' ') for x in c[i + 1].split('\n')])
nn = c[0].split(' ')
seen = []
for n in nn:
    seen.append(int(n))
    c = 0
    for i in range(100):
        if win(i):
            c += 1
        if c == 100:
            i = 93
            s = 0
            for j in range(5):
                for k in range(5):
                    if not(int(bb[i][j][k]) in seen):
                        s += int(bb[i][j][k])
            print(int(n) * s)
            break
    if c == 100:
        break
# part1 63552
# part2 9020
