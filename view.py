

#Getting which person is logging in
def personType():
    try:
        return "Press 1 if you are a librarian and 2 if you are an user: "
    except Exception as E:
        return E

#Registering the Librarian
def addLibrarian():
    return "Enter your name: "
def addLibrarianContact():
    return "Please enter your e-mail for contact information: "

#Getting book info from the librarian
def addBookOrUserOps():
    print("Press Y if you want to add books, N if not, Q if you want to delete books, E if you want to delete users")
def failedChoice():
    print("Oops, that was an incorrect key stroke. Try again!")
    addBookOrUserOps()

#If Y, the following executes
def bookName():
    return "Enter the name of the book: "
def bookAuthor():
    return "Enter the author of this book: "
def bookPublicationCompany():
    return "Enter the publication company of this book: "
def doneAdding():
    print("The book has been added successfully!")
def afterAdding():
    return "Enter Q to go to the main menu"
#If N, the following executes
def noBook():
    return "Enjoy your stay!"

#If Q, the following executes
def delBook(booksAvailable):
    for book in booksAvailable:
        print(book)
    return "Enter what book you want to delete by specifying it's ID number"
def delBookDone():
    print("The specified book has been deleted")

#If E, the following executes
def delUser(usersAvailable):
    for user in usersAvailable:
        print(user)
    return "Enter which user you want to delete by specifying his/her ID number"
def delUserDone():
    print("The specified user has been deleted")

#Getting the input if the user already exists or not
def existingUserOrNot():
    print("Hey there. Press 3 if you are an existing user, 4 if not")
    
def FailedexistingUserOrNot():
    print("Oops, that was an incorrect key stroke. Try again!")
    existingUserOrNot()

#Registering the user
def addUser():
    return "Enter the username: "
def addUserContact():
    return "Please enter your e-mail for contact information: "

def Congrats():
    print("Congratulations! Login with your username to continue")
    
#Login for the existing user    
def existingUser():
    return "Please enter your username: "
def Incorrect():
    print("Sorry, the entered username does not exist, try again")
    existingUser()
    
#If the username already exists in database, the following function executes
def alreadyExists():
    print("Sorry, the username you have entered already exists. Try another one")

def loggedIn():
    print("You have logged in!")
    return "Enter 0 if you want to see the books available and rent them, 1 if you want to update the username, 2 if you want to change the e-mail, R if you want to return any book"

def existingBooks(books):      #shows the list of books available
    for book in books:
        print(book)
    return "Enter what book you want to rent from the following list using the ID number"

def rented():
    print("You have rented the book")
    
#Updating user details
def newUserName():
    return "Enter the new username you want"
def userNameChanged():
    print("Your username has been changed!")
def newEmail():
    return "Enter the new email you want"
def emailChanged():
    print("Your email has been changed")
#Return Book and Add Fines
def returnBook():
    return "Enter the ID associated with the book that you want to return"
def FineAddedToUser(fineAdded):
    print(f"You have a fine of {fineAdded}")


 
