# Python program to illustrate function arguments

# ----------------------------------------------------------
# *args with first extra argument
def myFun1(arg1, *argv):
    print ("\n\n First argument :", arg1)
    for arg in argv:
        print(" Next argument through *argv :", arg)
 
# ----------------------------------------------------------
# **kargs for variable number of keyword arguments 
def myFun2(**kwargs):
    print("\n\n")
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

# ----------------------------------------------------------
# *args, **kargs for variable number of keyword arguments 

def myFun(*args,**kwargs):
    print("\n\n")
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 
# Driver code
myFun1('Hello', 'Welcome', 'to', 'BMU')
myFun2(first ='soharab', mid ='hossain', last='shaikh')
myFun('life','is','good',first="soharab",mid="hossain",last="shaikh")


