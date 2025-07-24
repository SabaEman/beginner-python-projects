# Project 3: Library Book Management System 📚

books = []

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        book_name = input("Enter book name: ")
        books.append(book_name)
        print(f"'{book_name}' added to the library.")

    elif choice == "2":
        print("\nBooks in Library:")
        for book in books:
            print("-", book)

    elif choice == "3":
        search = input("Enter book name to search: ")
        if search in books:
            print(f"'{search}' is available in the library.")
        else:
            print(f"'{search}' is NOT found.")

    elif choice == "4":
        print("Exiting Library. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")