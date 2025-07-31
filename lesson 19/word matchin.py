def matchwords(words):

    ctr = 0
    list = []

    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr = ctr + 1
            list.append(word)
    print("list of words with first and last character same is:", list) 
    return ctr

count = matchwords([ 'abc', 'xyz', 'aba', '1221', 'oqr'])
print("numbers of words having first and last character same is:", count)