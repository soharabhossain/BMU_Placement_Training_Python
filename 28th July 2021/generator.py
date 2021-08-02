
#-------------------------------------------------------------------------------

# In Python, to get a Finite sequence, you call range()
# and evaluate it in a list context:
a = range(5)
print(list(a))


#-------------------------------------------------------------------------------
# Generating an Infinite sequence, however, will require the use of a generator, since your computer memory is finite:

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# This code block is short and sweet.
# First, you initialize the variable num and start an infinite loop.
# Then, you immediately yield num so that you can capture the initial state.
# This mimics the action of range().

# After yield, you increment num by 1.
# If you try this with a for loop, then you’ll see that it really does seem infinite:

# You need to terminate this loop by pressing ctrl + c
#for i in infinite_sequence():
#   print(i, end=" ")
 

gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#-------------------------------------------------------------------------------
# Detecting Palindromes
# You can use infinite sequences in many ways, but one practical use for them is
# in building palindrome detectors.
# A palindrome detector will locate all sequences of letters or numbers that are palindromes.
# These are words or numbers that are read the same forward and backward, like 121.
# First, define your numeric palindrome detector:

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


#  Now you can use your infinite sequence generator to get a running list of all numeric palindromes:

# You need to terminate this loop by pressing ctrl + c
#for i in infinite_sequence():
#    pal = is_palindrome(i)
#    if pal:
#        print(pal)
    


#-------------------------------------------------------------------------------
# Building Generators With Generator Expressions

# Like list comprehensions, generator expressions allow you to quickly create a generator object in just a few lines of code.
# They’re also useful in the same cases where list comprehensions are used, with an added benefit:
# you can create them without building and holding the entire object in memory before iteration.
# In other words, you’ll have no memory penalty when you use generator expressions.
# Take this example of squaring some numbers:


nums_squared_lc = [num**2 for num in range(5)]

nums_squared_gc = (num**2 for num in range(5))



# Both nums_squared_lc and nums_squared_gc look basically the same, but there’s one key difference.

# This is a generator materialized in a List
print(nums_squared_lc)   # [0, 1, 4, 9, 16]

# This is a Generator object
print(nums_squared_gc)   # <generator object <genexpr> at 0x039016B8>


# Profiling Generator Performance
# Generators are a great way to optimize memory.
# While an infinite sequence generator is an extreme example of this optimization,
# let’s amp up the number squaring examples you just saw and inspect the size of
# the resulting objects. You can do this with a call to sys.getsizeof():

import sys
nums_squared_lc = [i * 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))       # 43808

nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))       # 56

# This means that the list is many times larger than the generator object!


# There is one thing to keep in mind, though.
# If the list is smaller than the running machine’s available memory, then list comprehensions
# can be faster to evaluate than the equivalent generator expression.
# To explore this, let’s sum across the results from the two comprehensions above.
# You can generate a readout with cProfile.run():

import cProfile

print(cProfile.run('sum([i * 2 for i in range(10000)])')) # 5 function calls in 0.005 seconds

print(cProfile.run('sum((i * 2 for i in range(10000)))')) # 10005 function calls in 0.019 seconds 

# Here, you can see that summing across all values in the list comprehension took about a third
# of the time as summing across the generator.
# If speed is an issue and memory isn’t, then a list comprehension is likely a better tool for the job.
#-------------------------------------------------------------------------------
