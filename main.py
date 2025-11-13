from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
print("Hello, you've entered the Library Management System!\n")
def view_available_books():


    print("Here's a list of our avaiable books:")
for book in library_books:
        if book['available']:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
print("\nHere's a list of our available books!")


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books():


    print("hello")
    search = input("\nWould you like to search by author or genre? (a/g):")
    if search == 'a':
        search_author = input("Please enter author name to search:").lower()
        for author in library_books:
            if author['author'].lower() == search_author:
                print(f"ID: {author['id']}, Title: {author['title']}, Author: {author['author']}")
    elif search == 'g':
        search_genre = input("Please enter genre to search:").lower()

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

#if __name__ == "__main__":
    # You can use this space to test your functions
    #pass
