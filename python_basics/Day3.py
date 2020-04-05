######################################################################################
# Printing Weird, Not weird, even and odd numbers on the basis of conditioal statements
# Task is:
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2  to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than 20 , print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints
# > 1 <= n <= 100
# ##################################################################################### 

def print_n():
    try:
        
        n = int(input("Please enter the integer").strip(" "))
        if (n % 2 != 0):
            print("weird")
        elif(n % 2== 0 & (2 <= n <= 5)):
            print("Not weird")
        elif(n % 2== 0 & (6 <= n <= 20)):
            print("Weird")
        elif(n % 2== 0 & (n > 20)):
            print("Not weird")
    except Exception as e:
        print(e)
        print_n()
print_n()

