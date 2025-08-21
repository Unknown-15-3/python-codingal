s1 = [1,2,3]
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1,s2))
print(s3)

list1 = [10,20,30,40,50]
list2 = [1,2,3,4,5]

for x, y in zip(list1, list2[::-1]):
    print(x,y)

stocks = ['reliance', 'infosys', 'tcs']
prices = [1280, 2100, 3500]

newdict = {stocks : price for stocks,price in zip(stocks, prices)}
print(newdict)