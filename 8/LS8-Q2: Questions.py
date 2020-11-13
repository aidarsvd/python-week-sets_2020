file = "answers.txt"

f = open(file, "w+")

a = str(input("What is your name and surname?"))
b = str(input("How old are you?"))
c = str(input("Where are you from?"))
d = str(input("What did you get on midterm exam?"))

f.write("{}%d\r\n".format(a))
f.write("{}%d\r\n".format(b))
f.write("{}%d\r\n".format(c))
f.write("{}%d\r\n".format(d))