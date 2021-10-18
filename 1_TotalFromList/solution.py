def total_from_list(arr, total):
    """
    Find all pair combinations of numbers in @member{arr} which sum up to @member{total}

    Time complexity = O(n) + O(n/2) = O(3n/2) = O(n)
    """
    sum_dict = {}
    ret_values = []

    # This loop takes O(n) time
    for num in arr:
        sum_dict[total - num] = num
    

    # This loop takes O(n/2) time
    for num in arr[:int(len(arr)/2+1)]:
        if num in sum_dict:
            ret_values.append((num, sum_dict[num]))

    return ret_values

    
# Identify edge cases
print(total_from_list([],0))
print(total_from_list([1],1))
print(total_from_list([1, 1],2))
print(total_from_list([1, 2, -1, 3],2))
print(total_from_list([10, 15, 3, 7, 14], 17))
