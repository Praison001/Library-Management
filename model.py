import datetime
from dateutil.relativedelta import relativedelta
from mysql.connector import MySQLConnection
from configparser import ConfigParser

#Reading the configuration and credentials from the config file and parsing it
def read_config(filename='config.ini',section='mysql'):
    parser=ConfigParser()
    parser.read(filename)
    db={}
    items=parser.items(section)
    #adding the parsed items to a dictionary
    for item in items:               
        db[item[0]]=item[1]
    return db

def InsertingLibrarian(librarianName,librarianContact):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query1= "INSERT INTO librarian (name,email) VALUES (%s,%s)"
    cursor.execute(query1,(librarianName,librarianContact,))
    connection.commit()
    connection.close()
def insertingUser(userName,userContact):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query10="INSERT INTO users(username,email) VALUES(%s,%s)"
    cursor.execute(query10,(userName,userContact,))
    connection.commit()
    connection.close()
def AddingBooks(bookN,bookAut,bookPubl):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query3= "INSERT INTO books (title, author, publication_company) VALUES(%s, %s, %s)"
    cursor.execute(query3,(bookN,bookAut,bookPubl,))
    connection.commit()
    connection.close()
def Verify(ExistingUserName):    #verify if the entered name is in the database or not
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    
    query= 'SELECT username from users WHERE username=%s'
    cursor.execute(query,(ExistingUserName,))
    res= cursor.fetchone()
    if res:
        return "Exists"
    else:
        return "Doesn't exist"
    connection.close()
def getBooks():
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query4= "SELECT * FROM books"
    cursor.execute(query4)
    rows= cursor.fetchall()
    row_ls= []
    for row in rows:
        row_ls.append(row)
    return row_ls
    
def getSpecificBook(bookChoice):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    
    query5= "SELECT title FROM books WHERE ID=%s"
    cursor.execute(query5,(bookChoice,))
    row= cursor.fetchone
    return row
    
#Once the book is rented
def updateUserAndTime(ExistingUserName,bookChoice,bookChoice1):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    current_time= datetime.datetime.now()
    query6= "UPDATE books SET rented_date=%s WHERE ID=%s"
    cursor.execute(query6, (current_time,bookChoice))
    connection.commit()

    query7= "UPDATE books SET rented_user=%s WHERE ID=%s"
    cursor.execute(query7, (ExistingUserName,bookChoice))
    connection.commit()

    query77= "UPDATE users SET book=%s WHERE username=%s"
    cursor.execute(query77,(bookChoice1,ExistingUserName))
    connection.commit()
    connection.close()
def updateUserName(ExistingUserName,newUserName1):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query8= "UPDATE users SET username=%s WHERE username=%s"
    cursor.execute(query8, (newUserName1,ExistingUserName))
    connection.commit()
    connection.close()
def updateEmail(ExistingUserName,newEmail1):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query9= "UPDATE users SET email=%s WHERE username=%s"
    cursor.execute(query9, (newEmail1,ExistingUserName))
    connection.commit() 
    connection.close()
def DeletingBooks(bookToBeDel):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query12= "DELETE FROM books WHERE ID=%s"
    cursor.execute(query12,(bookToBeDel,))
    connection.commit()
    connection.close()
def getUsers():
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query13= "SELECT * FROM users"
    cursor.execute(query13)
    rows1= cursor.fetchall()
    row_ls1= []
    for row1 in rows1:
        row_ls1.append(row1)
    return row_ls1
    
def DeletingUsers(userToBeDel):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    query14= "DELETE FROM users WHERE ID=%s"
    cursor.execute(query14,(userToBeDel,))
    connection.commit()
    connection.close()

def ReturnBookAddFine(ExistingUserName,retBook):
    db_con=read_config()
    connection=MySQLConnection(**db_con)
    cursor= connection.cursor()
    
    query15= "SELECT rented_date from books WHERE ID=%s"
    cursor.execute(query15,(retBook,))
    BorrowedDate= cursor.fetchone
    returnedDate= datetime.datetime.now()     #the date when the book is returned
    difference= relativedelta(returnedDate,BorrowedDate) #calculate the difference between the two dates
    difference_days= difference.days
    Fine= (difference_days//5)*5  #Calculating the rent

    query16= "UPDATE users SET fee=%s WHERE username=%s"
    cursor.execute(query16,(Fine,ExistingUserName))
    connection.commit()
    if difference_days>20:
        return Fine
    else:
        return None
    connection.close()

    


    

    




    


