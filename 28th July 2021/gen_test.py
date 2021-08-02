#-----------------------------------------------

def city_generator():
    """ Generate list of cities"""
    yield("Gurgaon")
    yield("Delhi")
    yield("Bangalore")
    yield("Kolkata")

city = city_generator()
print(city)
print(next(city))
print(next(city))
print(next(city))
print(next(city))
#print(next(city))   

print('\n\n')
#-----------------------------------------------

def list_generator(lst):
 """ Generate elements from a list - one at a time"""
 for l in lst:
   yield l
    
list_gen = list_generator([11,22,35,49,56])
print(list_gen)

print(next(list_gen))
print(next(list_gen))
print(next(list_gen))
print(next(list_gen))
print(next(list_gen))
#print(next(list_gen)) # StopIteration - runtime error  

print('\n\n')

#-----------------------------------------------

def generate_ints(N):
   """Generate numbers from 0, 1,2....N-1"""
   for i in range(N):
       yield i

gen = generate_ints(3)
print(gen)
    
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen)) # StopIteration - runtime error

#--------------------------------------------------------
# Define the Fibonacci Generator
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a = 0
    b = 1
    counter = 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(5)

for x in f:
    print (x)

print('\n\n')
#--------------------------------------------------------
# Generating an infite iterator
def fibonacci():
    """Fibonacci numbers generator - infinite series"""
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

f = fibonacci()
print(f)

counter = 0
for x in f:
    print (x)
    counter += 1
    if (counter > 10):
        break 

#--------------------------------------------------------



    
