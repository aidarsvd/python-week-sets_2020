f = open("random_numbers.txt", "r")

num_raw = f.read()

num_raw_str = num_raw.split(" ")

num = [int(x) for x in num_raw_str]

a = 0

for i in range(len(num)):
    a += num[i]

done = a / len(num)

file = "out.txt"

f = open(file, "w+")

f.write(str(done))

