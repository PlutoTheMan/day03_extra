def multiplication_table(n):
    spaces = len(str(n*n)) * 2
    a = ""
    a = a.ljust(int(spaces/2))
    for i in range(1, n+2):
        for j in range(1, n+1):
            if i == 1:
                b = str(i * j)
                b = b.rjust(spaces)
                a += b
            else:
                b = str((i-1)*j)
                b = b.rjust(spaces)
                a += b
        print(a)
        a = str(i)
        a = a.rjust(int(spaces/2))


multiplication_table(5)
