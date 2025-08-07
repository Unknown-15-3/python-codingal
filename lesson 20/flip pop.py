def palindrome(r):
    e = len(r) -1
    s=0
    while s<e:
        if r[s] != r[e]:
            return False
        s = s + 1
        e = e - 1
    return True
    
r = (1,2,3,4,5,6,7)

if palindrome(r):
    print("the tuple is a palindrome")
else:
    print("the tuple is not palindrome")