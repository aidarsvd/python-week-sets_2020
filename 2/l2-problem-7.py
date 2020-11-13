try:
    a = int(input())

#0-6 night
#6-10 morning
#10-18 day
#18-24 evening

    day = [0, 6, 7, 9, 10, 18, 19, 24]


    if a >= day[0] and a <= day[1]:
        print("Good night!")

    elif a >= day[2] and a <= day[3]:
        print("Good morning!")

    elif a >= day[4] and a <= day[5]:
        print("Good day!")

    elif a >= day[6] and a <= day[7]:
        print("Good evening!")

    else:
        print('Not acceptable time.')

except ValueError:
    print('Not acceptable time.')