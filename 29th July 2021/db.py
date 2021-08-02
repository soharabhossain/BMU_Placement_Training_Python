import sqlite3

# Create a Table
#-------------------------------------
db=sqlite3.connect('test.db')

try:        
    cur =db.cursor()
    cur.execute('''CREATE TABLE student (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT (20) NOT NULL,
    age INTEGER,
    marks REAL);''')
    
    print ('table created successfully')

except: # in case of any error or if the table already exists
        # then this block will be executed
    print ('error in operation')
    db.rollback()

db.close()


'''
# Insert a record in the table
#-------------------------------------

db=sqlite3.connect('test.db')
qry="insert into student (name, age, marks) values('Raj', 20, 50);"
try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print ("one record added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()

'''
'''
# Insert multiple records in the table
#-------------------------------------

db=sqlite3.connect('test.db')
qry="insert into student (name, age, marks) values(?,?,?);"
students=[('Amar', 18, 70), ('Deepak', 25, 87)]
try:
    cur=db.cursor()
    cur.executemany(qry, students)
    db.commit()
    print ("records added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()

'''
#---------------------------------------------


# Read Records
'''
# Fetch records from the table
#-------------------------------------
db=sqlite3.connect('test.db')
sql="SELECT * from student;"
cur=db.cursor()
cur.execute(sql)
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)
db.close()

'''

#---------------------------------------------

#--------------------------------------
# Update a Record
# -------------------------------------
'''
db=sqlite3.connect('test.db')

# Fetch all records
sql="SELECT * from student;"
cur=db.cursor()
cur.execute(sql)
print('Records before update : ')
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)


qry="update student set age=? where name=?;"
try:
    cur=db.cursor()
    cur.execute(qry, (30,'Deepak'))
    db.commit()
    print("record updated successfully")
except:
    print("error in operation")
    db.rollback()

# Fetch all records
sql="SELECT * from student;"
cur=db.cursor()
cur.execute(sql)
print('Records after update : ')
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)

db.close()

'''


#--------------------------------------
# Delete a record
#--------------------------------------
db=sqlite3.connect('test.db')

# Fetch all records
sql="SELECT * from student;"
cur=db.cursor()
cur.execute(sql)
print('Records before delete : ')
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)


qry="DELETE from student where name=?;"
try:
    cur=db.cursor()
    cur.execute(qry, ('Deepak',))
    db.commit()
    print("record deleted successfully")
except:
    print("error in operation")
    db.rollback()


# Fetch all records
sql="SELECT * from student;"
cur=db.cursor()
cur.execute(sql)
print('Records after delete : ')
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)

db.close()
