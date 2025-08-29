class pair_element:

    def twosum(self, nums, target):
        Lookup = {}

        for i, num in enumerate(nums):
            if target - num in Lookup:
                return (Lookup[target-num], i)
            Lookup[num] = i

value = int(input("enter the sum of which you want to make this search for:"))
print("index1 = %d, index2 = %d" %pair_element().twosum((10,20,30,40,50,60,70),value))