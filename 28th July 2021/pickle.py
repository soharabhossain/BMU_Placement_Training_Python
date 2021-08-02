# ----------------------------------------------------------------

import pickle as pk

# Serialize
f = open("pic.pk","wb")
dct = {"name":"Raj", "age":23, "Gender":"Male","marks":75}
pk.dump(dct, f)
f.close()


# De-Serialize

f = open("pic.pk","rb")
d = pk.load(f)
print(d)
f.close()

# ----------------------------------------------------------------

class Person:
  def __init__(self, name, age):
     self.name=name
     self.age=age
  def show(self):
     print ("name:", self.name, "age:", self.age)

p1 = Person('Raj', 35)
print ("\n Pickling data....")
f = open("pickled.pk","wb")
pk.dump(p1,f)
f.close()
print ("\n Pickling completed....")

print ("\n Now Unpickling data....")
f = open("pickled.pk","rb")
p1 = pk.load(f)
p1.show()

# ----------------------------------------------------------------

dictn = {"text": "string", "none": None, "boolean": True, "number": 3.44, "int_list": [1, 2, 3]}

import json
 
print (json.dumps(dictn))

print (json.dumps(dictn, indent=4))

# ----------------------------------------------------------------



