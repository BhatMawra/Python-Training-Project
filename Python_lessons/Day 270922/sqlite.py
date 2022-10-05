# import sqlite3

# # connect to database
# conn = sqlite3.connect('student.db')

# # Create cursor
# c = conn.cursor()

# Creating a table
# c.execute("""CREATE TABLE students(
#                 Std_id          int
#                 ,FirstName       varchar(25)
#                 ,LastName        varchar (25)
#                 ,Address         varchar(30)               
# )""")

# many_inputs = [(1,'Anam','Rauf','Shalimar'),(2,'Zarka','Rashid','Soura'),(3,'Aamir','Paul','Shopian'),(4,'Ufaq','Khan','Mallabagh'),
#                (5,'Suriya','Rashid','Lal Bazar')]
# c.executemany("INSERT INTO students VALUES (?,?,?,?)",many_inputs)
# c.execute("SELECT * FROM students")
# std_list =(c.fetchall())
# print("Std_id" + "\t\t" + "FirstName" + "\t" "LastName" +"\t"+"Address")
# print("======          ==========      =========       =======")
# for item in std_list:
    
#     print(str(item[0]) + "\t \t" + item[1] + " \t \t" + item[2]+ " \t \t" + item[3])
      
    
# #================================================================================================================================================


# c.execute("SELECT rowid from students")
# std_list =(c.fetchall())
# print(std_list)

# conn.commit()
# conn.close()
