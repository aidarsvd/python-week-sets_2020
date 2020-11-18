s = input()
longest = s[0]
occur = s[0]
for i in s[1:]:
    if i >= occur[-1]:
        occur += i
        if len(occur) > len(longest):
            longest = occur
    else:
        occur = i
print ("Longest substring in alphabetical order is: {}".format(longest))