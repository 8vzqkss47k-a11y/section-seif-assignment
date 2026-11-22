
books = []

print("Library Management System")

while True:
    print("\n1. Add a book")
    print("2. View books")
    print("3. Borrow a book")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        print("\nAvailable Books:")
        if len(books) == 0:
            print("No books available.")
        else:
            for book in books:
                print("-", book)

    elif choice == "3":
        book = input("Enter book name to borrow: ")
        if book in books:
            books.remove(book)
            print("Book borrowed successfully!")
        else:
            print("Book not found.")

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Try again.")
