with open('d05.in', 'r') as f:
    content = f.read()
c = [x.split(' -> ') for x in content.split('\n')]
b = [[0 for i in range(1000)] for j in range(1000)]
for ii,jj in c:
    i = ii.split(',')
    j = jj.split(',')
    if i[0] == j[0]:
        if i[1] > j[1]:
            i[1], j[1] = j[1], i[1]
            for y in range(int(i[1]), int(j[1]) + 1):
                b[y][int(i[0])] += 1
        else:
            for y in range(int(i[1]), int(j[1]) + 1):
                b[y][int(i[0])] += 1
    if i[1] == j[1]:
        if i[0] > j[0]:
            i[0], j[0] = j[0], i[0]
        for x in range(int(i[0]), int(j[0]) + 1):
            b[int(i[1])][x] += 1
#m = max([max(x) for x in b])
print(sum([sum([1 for x in b[y] if x > 1]) for y in range(1000)]))
