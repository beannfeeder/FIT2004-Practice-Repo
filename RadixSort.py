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
        if len(str(element)) > max_column:
            max_column=len(str(element))
    #finished finding max_column, now do the operation
    for column in range(max_column,0,-1):
        #now, compare every element in new_list
        count_array = []
        for _ in range(base):
            count_array[_]=[]

        for element in (new_list):
            #finds val to put inside count array
            key = (element // (base**column))% base
            #after we get the key, append the item inside count-array
            count_array[key].append(element)
            
            #copied from countingsort
            index = 0
            for i in range(len(count_array)):
                item = i
                frequency = count_array[i]
                for j in range(len(frequency)):
                    new_list[index] = item
                    index += 1

    
    return new_list

def RadixSortAlpha(new_list):
    column_counter = 0

print(example_num)
print("hello world")
print(RadixSortNum(example_num))



