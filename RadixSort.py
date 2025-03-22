#sort column by column
#e.g. alphabetical, left to right
    # numbers, right to left
example_alpha= ["a","apple", "never","pear","racecar"]
example_num=[3,4,100,50,2000,642,30945]

#Key operation: (value // (base^col)) % base 
#dont use padding
#straight up terminate if len() is less than the column count
def RadixSortNum(new_list):
    base = 10
    max_column= 0
    #find max column
    for element in (new_list):
        if len(element) > max_column:
            max_column=len(element)
    #finished finding max_column, now do the operation
    for column in range(max_column,0,-1):
        #now, compare every element in new_list
        for element in (new_list):
            #skips the number if it doesnt have the digit
            if len(element)< column:
                continue
            #finds val to put inside count array
            val = element[column]
            key = (val // (base^column))% base
            #after we get the key, put the item inside count-array
            #instantiate count-array
            count_array = [None] * base
            for i in range(len(count_array)):
                count_array[i] =[]
            print("Count-Array:", count_array)

def RadixSortAlpha(new_list):
    column_counter = 0

def __main__():
    # Test case for RadixSortNum
    test_numbers = [3, 4, 100, 50, 2000, 642, 30945]
    print("Original list:", test_numbers)
    sorted_numbers = RadixSortNum(test_numbers)


