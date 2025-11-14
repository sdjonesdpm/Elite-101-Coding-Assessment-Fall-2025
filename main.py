from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
print("Hello, you've entered the Library Management System!\n")

def view_available_books():
    print("Here's a list of our available books:\n")
    for book in library_books:
        if book.get("available"):
            print(f"ID: {book["id"]}, Title: {book["title"]}, Author: {book["author"]}")
view_available_books()

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books():
    search_question = input("\nWould you like to search by author or genre? (a/g): ").lower()
    if search_question == 'a':
        search_author = input("Please enter author name to search: ").lower()
        matches = [lb for lb in library_books if lb.get('author').lower() == search_author]
        if matches == True:
            print("Here are our books by that author:")
            for author in matches:
                print(f"ID: {author["id"]}, Title: {author["title"]}, Author: {author["author"]}")
#figure out why neither print statement is working
#something must be wrong with my indentation
# get method might be better to use
#try lb.get("author")
#get author isnt working
        else:
            print("I dont think we have any books by that author.")
    elif search_question == 'g':
        search_genre = input("Please enter genre to search: ").strip().lower()
        matches = [lb for lb in library_books if lb.get('genre').lower() == search_genre]
        if matches:
            print("Here are our books in that genre:")
            for genre in matches:
                print(f"ID: {genre['id']}, Title: {genre['title']}, Genre: {genre['genre']}")
        else:
            print("No books found in that genre.")
    else:
        print("Please enter a valid option.")
search_books()

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

# (left as TODOs for further implementation)

if __name__ == "__main__":
    view_available_books()
    # call search_books() interactively if desired
    # search_books()


#Citations: https://docs.python.org/3/library/string.html, https://www.youtube.com/watch?v=6RAWUwWmlOg&list=PLR_yj1kstmmrtiO7O4lgv3M6Anm8bP5mV, https://www.youtube.com/watch?v=MZZSMaEAC2g&list=PLR_yj1kstmmrtiO7O4lgv3M6Anm8bP5mV&index=2, https://www.youtube.com/watch?v=4t10v2QmTHU&list=PLR_yj1kstmmrtiO7O4lgv3M6Anm8bP5mV&index=3