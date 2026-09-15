# made by LudesDecay
# 2026-09-11
# Library Management System
with open("booklist.txt", "r") as f:
        booklist = f.read().splitlines()
firstload = False

bookname = ""
def abook():
    book = input("Enter book name: ")
    booklist.append(book)
    print(f"Added {book} to library")
    with open("booklist.txt", "w") as f:
        for book in booklist:
            f.write(book + "\n")
    controls()
    menu()

def rbook():
    book = input("Enter a book name: ")
    if book.lower() in [b.lower() for b in booklist]: # Check if book exists
        for b in booklist:
            if b.lower() == book.lower():
                booklist.remove(b)
                break
        with open("booklist.txt", "w") as f: # Save updated list
            for book in booklist:
                f.write(book + "\n")
        print("Book deleted successfully!")
    controls()
    menu()

def sbook():
    book = input("Enter a book name: ")
    if book.lower() in [b.lower() for b in booklist]:
        print("Book in list")
    else:
        print("Book not in list")
    controls()
    menu()


def vbooks():
    print("books in list:")
    for i in booklist:
        print(i)
    controls()
    menu()



    

def intro():
    print(" ____________________________________________________________________ \n|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|  |\n|__|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|\n|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|\n|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|  |\n|__|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|\n|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|\n|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|  |\n|__|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|\n|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|\n|__|   __|__|_____|__|_____|__|_____|__|_____|__|_____|__|_____|__|  |\n|__|__|                                                        |   __|\n|   __|                   -+ludesimplelib+-                    |__|  |\n|__|  |________________________________________________________|__|  |\n|__|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|\n|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|\n|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|  |\n|__|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|\n|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|\n|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|  |\n|__|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|\n|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|\n|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|  |\n|__|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|   __|__|")
    print(" -------------------------------------------------------------------- ")
    print("                   welcome to ludes' simple library!")
    print(" -------------------------------------------------------------------- ")

def controls():
    print(" -------------------------------------------------------------------- ")
    print(" |                         add - add a book                         | ")
    print(" |                      remove - remove a book                      | ")
    print(" |                     search - look for a book                     | ")
    print(" |                    display - display all books                   | ")
    print(" |                      controls - show controls                    | ")
    print(" |                         exit - exit program                      | ")
    print(" -------------------------------------------------------------------- ")

def menu():
    
    
    firstload = True
    

    if firstload == True:
        string = input("")
        if string == "add":
            abook()
        elif string == "remove":
            rbook()
        elif string == "search":
            sbook()
        elif string == "display":
            vbooks()
        elif string == "controls":
            controls()
        elif string == "exit":
            return
        else:
            print("Invalid command, ensure spelling is correct and try again")
    
intro()
controls()
menu()



