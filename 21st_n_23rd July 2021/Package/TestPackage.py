'''
Package Name: Animals
Module names: Mammals & Birds
Class names inside the modules: Mammal & Bird
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# How to use? - Two approaches

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
# Approach 1
#--------------------------

#---------------------------------------------------------------
# Importing the Modules from the package Animals

from Animals import Mammals
from Animals import Birds

# Create an object of Mammals class & call a method of it
myMammal = Mammals.Mammal()
myMammal.printMembers()
 
# Create an object of Birds class & call a method of it
myBird = Birds.Bird()
myBird.printMembers()


'''

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Approach 2
#--------------------------

#--------------------------------------------------------------------------------------------------------
# Importing the classes from the package Animals and respective modules inside it
from Animals.Mammals import Mammal
from Animals.Birds import Bird

# Create an object of Mammals class & call a method of it
myMammal = Mammal()
myMammal.printMembers()
 
# Create an object of Birds class & call a method of it
myBird = Bird()
myBird.printMembers()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

