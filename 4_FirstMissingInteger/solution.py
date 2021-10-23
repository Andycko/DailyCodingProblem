def first_missing_integer(arr):
    """
    Time complexity of max() = O(n)
    Space complexity is constant 
    """
    # sorted = set(arr)
    # sorted = list(sorted)
    # for i, x in enumerate(sorted):
    #     if x > 0:
    #         if i != len(sorted) - 1:
    #             if sorted[i+1] - x != 1:
    #                 return x + 1
    #         else:         
    #             return x + 1 
    #     else:
    #         if i == len(sorted) - 1:
    #             return 1

    res = None
    for x in arr:
        if res == None:
            if x > 0:
                res = x
        elif x < res:
            res = x
    return res if res else 1

# Identify edge cases
# print(first_missing_integer([]), 1)
print(first_missing_integer([1]), 2)
print(first_missing_integer([-1,-2]), 1)
print(first_missing_integer([3, 2, 1]), 4)
print(first_missing_integer([7,8,9,11,12]), 10)
print(first_missing_integer([1, 2, -1, 3]), 4)
print(first_missing_integer([3, 4, -1, 1] ), 2)
