with open('d02.in', 'r') as f:
    d = f.readlines()
    dd = [x.replace('\n', '').split(' ') for x in d]
    a = x = y = 0
    for i in dd:
        if i[0] == 'forward':
            x += int(i[1])
            y += a * int(i[1])
        if i[0] == 'up':
            a -= int(i[1])
        if i[0] == 'down':
            a += int(i[1])
    print(x * y)  # part1 1938402, part2 1947878632
