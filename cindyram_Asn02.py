"""
CS1026A 2023
Assignment 02 
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
October 23, 2023
"""

# Define the start function to manage the library system.
def start():
    # Initialize a list of all books with some sample data.
    allBooks = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]

    # Initialize a list of rented books (books currently borrowed).
    borrowedISBNs = []

    # Start an infinite loop to display the menu and handle user input.
    while True:
        # Display the main menu.
        printMenu()
        selected_menu = input("Your selection>")

        # Handle user's menu choice.
        if selected_menu.lower() == "1" or selected_menu.lower() == "a":
            # Option 1: Add a new book.
            new_book = addBook(allBooks)
            if not ISBN_exist(new_book[0], allBooks):
                allBooks.append(new_book)
            else:
                print("Selected ISBN already exists on the list.")

        elif selected_menu.lower() == "2" or selected_menu.lower() == "r":
            # Option 2: Borrow books.
            borrower_name = input("Enter the borrower name> ")
            matching_books = []

            # Iterate through the books to find matching books.
            for book in allBooks:
                borrowers = [borrower.lower() for borrower in book[4]]
                
                if borrower_name.lower() not in borrowers:
                    search_term = input("Search term> ")

                    if search_term.endswith("*"):
                        # Search by a partial book name.

                        search_term = search_term[:-1]
                        # Loop to check if the input match with the books in the list, and store it to variable
                        matching_books = [book for book in allBooks if search_term.lower() in book[1].lower()]

                        # Loop to assign the name of borrower to every possible books
                        for matching_book in matching_books:
                            if matching_book not in borrowedISBNs:
                                matching_book[4].append(borrower_name)
                                borrowedISBNs.append(matching_book)
                                print(f'\t-"{matching_book[1]}" is borrowed!')
                        break

                    elif search_term.endswith("%"):
                        # Search by a book name prefix.
                        search_term = search_term[:-1]

                        # Loop to check if the input match with the books in the list, and store it to variable
                        matching_books = [book for book in allBooks if book[1].lower().startswith(search_term.lower())]

                        # Loop to assign the name of borrower to every possible books
                        for matching_book in matching_books:
                            if matching_book not in borrowedISBNs:
                                matching_book[4].append(borrower_name)
                                borrowedISBNs.append(matching_book)
                                print(f'\t-"{matching_book[1]}" is borrowed!')
                        break

                    else:
                        # Search for an exact book name match.
                        matching_books = [book for book in allBooks if book[1].lower() == search_term.lower()]
                        
                        # Loop to assign the name of borrower to every possible books
                        for matching_book in matching_books:
                            if matching_books not in borrowedISBNs:
                                matching_book[4].append(borrower_name)
                                borrowedISBNs.append(matching_book)
                                print(f'\t-"{matching_book[1]}" is borrowed!')
                        break

            # If no matching books are found, display a message.
            if not matching_books:
                print("No books found!")

        elif selected_menu.lower() == "3" or selected_menu.lower() == "t":
            # Option 3: Return a book.
            book_isbn = input("ISBN> ")

            # Loop to check if the input match with the books in the list, and store it to variable
            matching_books = [book for book in borrowedISBNs if book[0] == book_isbn]

            # If the result is true
            if matching_books:
                for matching_book in matching_books:
                    borrowedISBNs.remove(matching_book)
                    print(f'"{matching_book[1]}" is returned.')
            elif matching_books == False:
                print(f'"{matching_book[1]}" is not borrowed.')
            else:
                print("No book is found!")

        elif selected_menu.lower() == "4" or selected_menu.lower() == "l":
            # Option 4: List all books.
            for books in allBooks:
                if books not in borrowedISBNs:
                    print("---------------")
                    print("[Available]")
                    print(f"{books[1]} - {books[2]}")
                    print(f"E: {books[3]} ISBN: {books[0]}")
                    print(f"Borrowed by: {books[4]}")
                else:
                    print("---------------")
                    print("[Unavailable]")
                    print(f"{books[1]} - {books[2]}")
                    print(f"E: {books[3]} ISBN: {books[0]}")
                    print(f"Borrowed by: {books[4]}")

        elif selected_menu.lower() == "5" or selected_menu.lower() == "x":
            # Option 5: Exit the program.
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")

            for books in allBooks:
                if books not in borrowedISBNs:
                    print("---------------")
                    print("[Available]")
                    print(f"{books[1]} - {books[2]}")
                    print(f"E: {books[3]} ISBN: {books[0]}")
                    print(f"Borrowed by: {books[4]}")
                else:
                    print("---------------")
                    print("[Unavailable]")
                    print(f"{books[1]} - {books[2]}")
                    print(f"E: {books[3]} ISBN: {books[0]}")
                    print(f"Borrowed by: {books[4]}")
            exit()

        else:
            # Handle invalid menu selections.
            print("Wrong selection! Please select a valid option")

# Function to display the main menu.
def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')

# Function to check the validity of an ISBN.
def ISBN_checker(ISBN):
    total = 0

    # Iterate through the 13-digit ISBN.
    for i in range(13):
        digit = int(ISBN[i])
        
        # Weight for even-positioned digits.
        if i % 2 == 0:
            weight = 1  
        # Weight for odd-positioned digits.
        else:
            weight = 3  
        total += digit * weight

    if total % 10 == 0:
        return total

# Function to check if an ISBN already exists in the list of books.
def ISBN_exist(isbn, book_list):
    for book in book_list:
        if book[0] == isbn:
            return True
    return False

# Function to add a new book to the library system.
def addBook(allBooks):
    borrower = []  # Create an empty list of borrowers for the new book.

    while True:
        book_name = input("Enter book name> ")
        if "%" not in book_name and "*" not in book_name:
            book_author = input("Author name> ")
            if book_author != "" and len(book_author) > 1:
                while True:
                    book_edition = input("Edition> ")
                    if book_edition.isdigit():
                        while True:
                            book_isbn = input("ISBN> ")
                            if len(book_isbn) < 13:
                                print("Invalid ISBN!")
                            elif not (book_isbn.isdigit() and len(book_isbn) == 13 and ISBN_checker(book_isbn)):
                                print("Invalid ISBN!")
                                start()  # Restart if ISBN is invalid.
                            elif any(book_isbn == book[0] for book in allBooks):
                                print("Duplicate ISBN is found! Cannot add the book.")
                                start()  # Restart if ISBN is a duplicate.
                            else:
                                print("A new book has been added successfully.")
                                book_complete = [book_isbn, book_name, book_author, book_edition, borrower]
                                return book_complete
                    else:
                        print("Insert a valid number!")
            else:
                print("Author name is invalid!")
        else:
            print("Invalid book name!")

# Invoke the start function to run the library system.
start()