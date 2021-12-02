with open('d01.in', 'r') as f:
    d = f.readlines()
c = s = x = y = z = 0
for i in d:
    z = y
    y = x
    x = int(i)
    if x + y + z > s:
        c += 1
    s = x + y + z
# print(c - 1)  # part1 1195, subtract the 1st
print(c - 3)  # part2 1235, subtract the 1st 3
