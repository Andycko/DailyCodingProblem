def product_from_rest(arr):
    """
    Time complexity = O(n) + O(n) = O(2n) = O(n)
    """

    product = 1
    res = []
    for num in arr:
        product = product * num

    for num in arr:
        res.append(product//num)
    
    return res
    

    # Naive approach (without division) - Time complexity = O(n^2)
    #
    # res = []
    # for i_num, _ in enumerate(arr):
    #     res.append(1)
    #     for i_x, x in enumerate(arr):
    #         if i_x != i_num:
    #             res[i_num] = res[i_num] * x
    # return res

    
# Identify edge cases
print(product_from_rest([]), [])
print(product_from_rest([1]), [])
print(product_from_rest([1, 2, -1, 3]), [-6, -3, 6, -2])
print(product_from_rest([1, -2, -1, 3]), [6, -3, -6, 2])
print(product_from_rest([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
print(product_from_rest([3, 2, 1]), [2, 3, 6])
