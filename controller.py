import model
import view
import datetime

def getPersonType():
  
    choice= input(view.personType())     #getting the input if the librarian or the user wants to use 

    #For Librarian
    if choice=='1':   
        librarianName= input(view.addLibrarian())
        librarianContact= input(view.addLibrarianContact())
        model.InsertingLibrarian(librarianName,librarianContact)
        librarianOps()

    #For User
    elif choice=='2':
        existingUserOrNot= input(view.existingUserOrNot())
        #Existing user
        if existingUserOrNot=='3':
            ExistingUserName= input(view.existingUser())
            
            #Check if the user exists in the database
            verified= model.Verify(ExistingUserName)
            if verified=="Exists":
                desired_choice=input(view.loggedIn())

                if desired_choice=="0":
                    bookOps(ExistingUserName)
                    
                elif desired_choice=="1":
                    userOps(ExistingUserName)
                    
                elif desired_choice=="2":
                    emailOps(ExistingUserName)
                
                elif desired_choice=="R" or desired_choice=="r":
                    ReturnBook(ExistingUserName)

            elif verified=="Doesn't exist":
                view.Incorrect()

        #Registering the new user
        elif existingUserOrNot=='4':                 
            regNewUser()
        else:
            view.FailedexistingUserOrNot()

def regNewUser():
    userName= input(view.addUser())
    userContact= input(view.addUserContact())
    
    #check if the entered username already exists in the database
    verified= model.Verify(userName)
    if verified=="Exists":
        view.alreadyExists()
        regNewUser()
    elif verified=="Doesn't exist":
        model.insertingUser(userName,userContact)  #saving the new user in the database
        view.Congrats()
        #requesting the user to login with the registered username
        ExistingUserName= input(view.existingUser())

        #Check if the user exists in the database
        verified= model.Verify(ExistingUserName)

        if verified=="Exists":
            desired_choice=input(view.loggedIn())
            if desired_choice=="0":
                bookOps(ExistingUserName)
            elif desired_choice=="1":
                userOps(ExistingUserName)
            elif desired_choice=="2":
                emailOps(ExistingUserName)
            elif desired_choice=="R" or desired_choice=="r":
                    ReturnBook(ExistingUserName)
                    
        elif verified=="Doesn't exist":
            view.Incorrect()

def librarianOps():
    librarianAddBook= input(view.addBookOrUserOps())  #gets the choice of operation that the librarian wants to perform
    #following block is executed if the librarian wants to add books
    if librarianAddBook=='Y' or librarianAddBook=='y':
            
        bookN= input(view.bookName())
        bookAut= input(view.bookAuthor())
        bookPubl=input(view.bookPublicationCompany())
        model.AddingBooks(bookN,bookAut,bookPubl) 
        view.doneAdding()
        afterAdd= input(view.afterAdding())

        if afterAdd=='Q' or afterAdd=='q':
            librarianOps() #calls the function again recursively to go back to the start

    #following block is executed if the librarian doesn't want to add any books
    elif librarianAddBook=='N' or librarianAddBook=='n':
        #Nothing happens if the libraian chooses N
        view.noBook()

    #following block is executed if the librarian wants to delete any book
    elif librarianAddBook=='Q' or librarianAddBook=='q':
        booksAvailable= model.getBooks()
        bookToBeDel= input(view.delBook(booksAvailable)) #bookToBeDel contains the ID of the book to be deleted
        model.DeletingBooks(bookToBeDel)
        view.delBookDone()

    #following block is executed if the librarian wants to delete any user
    elif librarianAddBook=='E' or librarianAddBook=='e':
        usersAvailable= model.getUsers()
        userToBeDel= input(view.delUser(usersAvailable)) #userToBeDel contains the ID of the user to be deleted
        model.DeletingUsers(userToBeDel)
        view.delUserDone()

    else:
        #If the user enters an incorrect key stroke
        view.failedChoice()

def bookOps(ExistingUserName):
    #get the list of books available
    books= model.getBooks()
    bookChoice= input(view.existingBooks(books)) #bookChoice contains the ID of the book
    #fetching the book as well as updating the rented user and rented time
    bookChoice1= model.getSpecificBook(bookChoice) #bookChoice1 contains only the title of the book
    #Updating the time the book was rented using datetime and also the rented user in the books and users tables
    model.updateUserAndTime(ExistingUserName,bookChoice,bookChoice1)
    view.rented()

def userOps(ExistingUserName):
    #Updating the username
    newUserName1= input(view.newUserName())
    model.updateUserName(ExistingUserName,newUserName1)
    view.userNameChanged()

def emailOps(ExistingUserName):
    #Updating the email
    newEmail1= input(view.newEmail())
    model.updateEmail(ExistingUserName,newEmail1)
    view.emailChanged()

def ReturnBook(ExistingUserName):
    retBook= int(input(view.returnBook()))
    fineAdded= model.ReturnBookAddFine(ExistingUserName,retBook)
    view.FineAddedToUser(fineAdded)
    
print(getPersonType())



    










