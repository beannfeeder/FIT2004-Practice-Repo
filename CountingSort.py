def CountingSort(new_list):
    #new_list will be sorted
    #find the maximum value
    #build count-array
    #go throuhg input list and update the count-array
    #loop through count array to rebuild the original list (sorted)
    """
    Precondition: new_list must have at least 1 item
    """
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item
        print(max_item)
    
    #build count-array
    count_array = [0] * (max_item +1) 
    print(count_array)

    #update count-array
    for item in new_list:
        count_array[item] = count_array[item] + 1
        #searches through the input list and updates the count-array
    print("Count-array:", count_array)

    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item
            index += 1

    return new_list



a_list = [5, 2, 9, 5, 2, 3, 5]
print("Sorted List:", CountingSort(a_list))
for i in range(0, len(a_list)):
    if a_list[i] <= list_a[i+1]:
        continue
    else:
        print("fail!")
        break
print("pass!")