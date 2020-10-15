# def sortedd (numbers):
# 	a = sorted(numbers)
# 	return a
#
# c_raw = input()
#
# v = c_raw.split(" ")
# b = []
#
# for i in range(len(v)):
# 	b.append(int(v[i]))
#
# print(sortedd(b))
#
#




# def listOddEven(nums):
# 	x = []
# 	c = []
# 	for i in range(len(nums)):
# 		if nums[i] % 2 == 0:
# 			x.append(nums[i])
# 		else:
# 			c.append(nums[i])
# 
# 	print(sorted(c))
# 	print(sorted(x))
# 
# 
# 
# raw_nums = input()
# nums = raw_nums.split(",")
# x = []
# for i in range(len(nums)):
# 	x.append(int(nums[i]))
# 
# listOddEven(x)
#
# l = input()
# a = l.lower()
# b = a.split(" ")
#
# c = list(dict.fromkeys(b))
#
# lil = sorted(c)
# # b list
#
# dick = {}
#
# big = []
# for i in range(len(lil)):
# 	big.append(lil[i].upper())
#
# for i in range(len(lil)):
# 	dick[big[i]] = lil[i]
#
# bigdick = sorted(dick.items(), key=lambda x: x[1], reverse=False)
#
# print(bigdick)
#
#
# u = input()
# chars = "abcdefghijklmnopqrstuvwxyz"
# check_string = u.lower()
# lets = []
# nums = []
# for char in chars:
# 	count = check_string.count(char)
# 	if count >= 1:
# 		lets.append(char)
# 		nums.append(count)
#
#
# alph = {}
# for i in range(len(lets)):
# 	alph[lets[i]] = nums[i]
#
#
# dictionary_items = alph.items()
# sorted_items = sorted(dictionary_items)
# print(sorted_items)

# a = input()
# test_list = a.split(" ")
# for i in range(0, len(test_list)):
#     test_list[i] = int(test_list[i])
# b = sorted(test_list)
# print(b)

#
a = input()
b = []
for i in range(len(a)):
	b.append(a[i])
if "ing" in a and len(b) >= 3:
	b.remove("i")
	b.remove("n")
	b.remove("g")
	b.append("l")
	b.append("y")
elif "ing" not in a and len(b) >= 3:
	b.append("i")
	b.append("n")
	b.append("g")
else:
	pass
c = "".join(b)
print(c)

# a = input()
# b = input()
# c = []
# d = []
# for i in range(len(a)):
# 	c.append(a[i])
# for i in range(len(b)):
# 	d.append(b[i])
# raw_word = [d[0],d[1], c[2]]
# raw_word2 = [c[0],c[1], d[2]]
# word = "".join(raw_word)
# word2 = "".join(raw_word2)
# done_word = f"{word} {word2}"
# print(done_word)




