import os
import json

# File to store the library
LIBRARY_FILE = 'library.txt'

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, 'w') as f:
        json.dump(library, f, indent=4)

# Display menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = read_input == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the search term: ").lower()
    
    matches = []
    if choice == '1':
        matches = [book for book in library if keyword in book['title'].lower()]
    elif choice == '2':
        matches = [book for book in library if keyword in book['author'].lower()]
    else:
        print("Invalid choice.")
        return

    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

# Display all books
def display_all_books(library):
    if not library:
        print("Library is empty.")
    else:
        print("Your Library:")
        for i, book in enumerate(library, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("Library is empty.")
    else:
        read_books = sum(1 for book in library if book['read'])
        percentage = (read_books / total) * 100
        print(f"Total books: {total}")
        print(f"Percentage read: {percentage:.1f}%")

# Main function
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
