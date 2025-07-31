list = [ 1, 23, 32, 12, 36, 42, 5, 10, 50, 43, 21, 17, 18]
print("original list", list)

sum = 0
for i in list:
    sum = sum + i

avg = sum/ len(list)

print("sum of the list is:", sum)
print("average of the lisy is:", avg)

list.sort()
print("the smallest elemnt in the list:", list[0])
print("the largest elemnt in the list:", list[-1])