with open('d03.in', 'r') as f:
    d = f.readlines()
dd = [x.replace('\n', '') for x in d]
g = ''
for k in range(len(dd[0])):
    if [x[k] for x in dd].count('1') >= len(dd)/2:
        g = g + '1'  # swap these for part2
    else:
        g = g + '0'  # swap these for part2
    ddd = [x for x in dd if x[0:k+1] == g]
    dd = ddd
    if len(dd) == 1:
        g = dd[0]
        break
gg = int(g, 2)
print(gg * (4095 - gg))  # part1 3633500, part2 1947878632
# part2 1327 * 3429 = 4550283
