try:
    a = [93, 100, 4.0]

    am = [90, 92, 3.67]

    bp = [87, 89, 3.33]

    b = [83, 86, 3.0]

    bm = [80, 82, 2.67]

    cp = [77, 79, 2.33]

    c = [70, 76, 2.0]

    d = [60, 69, 1.0]

    f = [0, 59, 0.0]

    grade = float(input())

    if grade >= a[0] and grade <= a[1]:
        print("A {}".format(a[2]))

    elif grade >= am[0] and grade <= am[1]:
        print("A- {}".format(am[2]))

    elif grade >= bp[0] and grade <= bp[1]:
        print("B+ {}".format(bp[2]))

    elif grade >= b[0] and grade <= b[1]:
        print("B {}".format(b[2]))

    elif grade >= bm[0] and grade <= bm[1]:
        print("B- {}".format(bm[2]))

    elif grade >= cp[0] and grade <= cp[1]:
        print("C+ {}".format(cp[2]))

    elif grade >= c[0] and grade <= c[1]:
        print("C {}".format(c[2]))

    elif grade >= d[0] and grade <= d[1]:
        print("D {}".format(d[2]))

    elif grade >= f[0] and grade <= f[1]:
        print("F {}".format(f[2]))

    else:
        print("Incorrect grade!")

except ValueError:
    print("Incorrect grade!")