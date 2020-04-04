import sys

a = ['a',2,4]
for each in a:
    try:
        r =1/int(each)
        print(r)
    except:
        print("The error occured is {} {} at Line Number is:{}".format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
    else:
        print("I am from else block")
    finally:
        print("No matter, I am from Finally block and getting executed")
        print("committed to git successfully ")