def largest_in_list(list):
    largest = None
    for current_number in list:
        if largest == None:
            largest = current_number
        elif current_number > largest:
            largest = current_number
    return largest 

result = largest_in_list([1,2,3,45,6,7,98])
print("{} is the largest number from the list provided!".format(result))
