from datetime import datetime, timedelta

# Predefined list of books
catalog = {
    "001": {"title": "Book 1", "author": "Author 1", "quantity": 5},
    "002": {"title": "Book 2", "author": "Author 2", "quantity": 3},
    "003": {"title": "Book 3", "author": "Author 3", "quantity": 7}
}

# Dictionary to store user information
users = {}

# Dictionary to store book transactions
transactions = {}

# Function to display current catalog
def display_catalog():
    print("Current Catalog:")
    for book_id, book_info in catalog.items():
        print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Quantity Available: {book_info['quantity']}")

# Function for user registration
def register_user(user_id, name):
    if user_id not in users:
        users[user_id] = {"name": name, "books_checked_out": []}
        print("User registered successfully.")
    else:
        print("User ID already exists.")

# Function for book checkout
def checkout_book(user_id, book_id):
    if user_id not in users:
        print("User not registered.")
        return
    if book_id not in catalog:
        print("Book not found.")
        return
    if len(users[user_id]["books_checked_out"]) >= 3:
        print("Maximum books checkout limit reached.")
        return
    if catalog[book_id]["quantity"] == 0:
        print("Book not available.")
        return
    
    # Record checkout transaction
    users[user_id]["books_checked_out"].append(book_id)
    catalog[book_id]["quantity"] -= 1
    transactions[book_id] = {"user_id": user_id, "checkout_date": datetime.now()}
    print("Book checked out successfully.")

# Function for book return
def return_book(book_id):
    if book_id not in transactions:
        print("Book not checked out.")
        return
    
    user_id = transactions[book_id]["user_id"]
    checkout_date = transactions[book_id]["checkout_date"]
    due_date = checkout_date + timedelta(days=14)
    return_date = datetime.now()
    fine = max(0, (return_date - due_date).days) * 1
    
    # Update catalog and transaction records
    catalog[book_id]["quantity"] += 1
    users[user_id]["books_checked_out"].remove(book_id)
    del transactions[book_id]
    
    if fine > 0:
        print(f"Book returned successfully. Fine due: ${fine}")
    else:
        print("Book returned successfully.")

# Function to list overdue books for a user
def list_overdue_books(user_id):
    overdue_books = []
    total_fine = 0
    for book_id, transaction_info in transactions.items():
        if transaction_info["user_id"] == user_id:
            checkout_date = transaction_info["checkout_date"]
            due_date = checkout_date + timedelta(days=14)
            if datetime.now() > due_date:
                overdue_books.append(book_id)
                days_overdue = (datetime.now() - due_date).days
                fine = days_overdue * 1
                total_fine += fine
    
    if overdue_books:
        print("Overdue Books:")
        for book_id in overdue_books:
            print(f"Book ID: {book_id}, Fine: ${fine}")
        print(f"Total Fine: ${total_fine}")
    else:
        print("No overdue books.")

# Sample usage of functions
if __name__ == "__main__":
    display_catalog()
    register_user("001", "John")
    checkout_book("001", "001")
    checkout_book("001", "002")
    return_book("001")
    list_overdue_books("001")
