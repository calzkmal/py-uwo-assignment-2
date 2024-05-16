# py-uwo-assignment-2
Created a menu-driven program that is used for simple library system. Implementing some functionalities to add books to the library and borrow/return books.

# Long Code Description
*1* Implement the function start() that takes no parameters and doesn't return anything. This function is the entry point for your program and must be invoked once.
Modularize the code by separating it into multiple functions where each function is responsible to accomplish a specific task. The names, number of functions, and the breakdown is left up to user. 

*2* Within the function start() build a menu that offers the user several options as follows:
1: (A)dd a new book.
2: Bo(r)row books.
3: Re(t)urn a book.
4: (L)ist all books.
5: E(x)it.
The user can select one option at a time by either typing the number of the option OR the letter enclosed by the brackets. The program neglects the case of the typed letter i.e., if the user types 3 or t or T, this means that "Return a book is selected". If the users enters an invalid option such as Y or 9, a warning message shows up "Wrong selection! Please selection a valid option." and the menu is dispayed again.

*3* Add a new book. This option is selected when the user wants to add a new book to the available list of books. To add a new book you should ask the user to enter 4 peices of information:
Book name: A string.
Author: A string.
Edition: An integer.
International Standard Book Number (ISBN): A unique 13 digits number.

*4* The user is first asked to enter the book name. The book name may be of any length, any may have any characters except the star * and the percent % . If the user includes * or % in the book name, an error message is shown and the program keeps asking the user for a valid name. A while loop is a good fit for such task.

*5* The user is then asked to enter the author name. No validation is required for this.

*6* The user is then asked to enter the edition of the book. The book edition is an integer. If a decimal number is entered, the integer part is considered . If the user enters a decimal point number or a non-numeric value (such as "a1" or "hi" or"3#") an error message is shown and the program keeps asking the user for a valid number.

*7* The user is then asked to enter the ISBN of the book. The book ISBN is a 13-digit integer. If the user enters a non-numeric value (such as "asdf" or "123456789aaa") an error message is shown and the program keeps asking the user for a valid ISBN.

Once a 13-digit is entered, the ISBN should be checked for validity. To check for a valid ISBN, use the steps below::
Multiply each digit of the ISBN from left to right by a specific weight factor: 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1.
Sum the results of these multiplications.
If the sum of the multiplications is multiple of 10, then the ISBN is valid, otherwise is it invalid.
For example, if the ISBN is 9783161484109 then the sum of the multiplications = 9x1 + 7x3 + 8x1 + 3x3 + 1x1 + 6x3 + 1x1 + 4x3 + 8x1 + 4x3 + 1x1 + 0x3 + 9x1 = 109. This ISBN is invalid since 109 is not a multiple of 10.

If the 13-digit number is not a valid ISBN, this book entry is skipped and the program returns to the main menu (no repetitive checking is required)
Once the ISBN is validated, the entered value is compared against all ISBNs of the already available books. If the entered value is already found, this book entry is skipped and the program returns to the main menu (no repetetive checking is required). Otherwise, all book information is valid at this moment and this information will be stored in a list of books (let us call it allBooks ). The book information is stored in a list in the following order:
oneNewBook = [isbn, bookName, author, edition,[]]
the last empty list will be used to store the names of people who will borrow this book. It acts as the history of the previous borrowers of the book. More on this later.

*8* Borrow Books. A user select this option when someone wants to borrow book(s).

*9* The user is first asked to enter the name of the borrower. No validation is required here.

*10* The user is then asked to search for books using a search term. In this program, three search modes are available:
Contains: If the user enters a term ending with a star * this means that the term may be found anywhere in the book name. For example, considering the allBooks list above, if the user enters eart* the two books "The Earth Inside Out" and "Human on Earth" are found. You can assume that the user will always enter a valid search term.
Starts with: If the user enters a term ending with a percent % this means that the term may be found only at the beginning of the book name. For example, considering the allBooks list above, if the user enters the% the two books "The Earth Inside Out" and "The Human Body" are found. You can assume that the user will always enter a valid search term.
Exact: If the user enters a term without any suffix this means that the term may be found only if the term exactly matches the book name. For example, considering the allBooks list above, if the user enters HumAn ON earth the books "Human on Earth" is found only.
If there is no matches to the search term, a warning message should be dispalyed the no books were found. Again, everything here is case insensitive.

*11* Once the search is applied and a list of matching books are found, ALL the matching books will be borrowed under the name of the borrower. You need to append the borrower's name to the borrowers list (the empty list that we initially added as the 5th item of the book list). Note that this list holds the names of the previous borrowers (history) and the current borrower's name. If the book is being borrowed for the first time, the borrower name is appended to an empty list. 

*12* The list accumulates names as the book is getting borrowed and returned over time.

*13* In this assignment, we assume that this library has a single copy of each book. If the book is borrowed, then it will not be available until it is returned.
You need to find a mechanism to track the books that are currently borrowed by someone. A list of ISBNs of the borrowed books (let us call it borrowedISBNs) may be a good idea.

*14* Return A Book. This option is selected if the user wants to return a book. This means after a book is returned, this book becomes available and will appear in the next search results.

*15* The user is first asked to enter the ISBN of the book to return.

*16* The ISBN is compared with all ISBN numbers of the borrowed books (borrowedISBNs). If a match is found, this ISBN is simply removed from this list to make it available. Otherwise, a warning message should show "No book is found!", and the execution returns to the main menu.

*17* List All Books. This option is selected if the user wants to show all books in the system. 

*18* Exit. This option is selected whenever the user wants to quit the program. When selected, the exact following message is displayed ( 8 dollar signs $$$$$$$$ from each side):
$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$
And then all books are printed in the exact format of the previous option List all books.
