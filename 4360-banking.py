import json

# Data storage file
DATA_FILE = 'bank_data.json'

# Load data from file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add new user
def add_user():
    data = load_data()
    
    name = input("Enter new user's name: ")
    password = input("Enter new user's password: ")
    initial_balance = float(input("Enter initial balance for the new user: "))
    
    new_user = {
        "name": name,
        "password": password,
        "balance": initial_balance
    }
    
    data["users"].append(new_user)
    save_data(data)
    print("New user added successfully!")

# User authentication
def login(username, password):
    data = load_data()
    print(f"Trying to login with username: {username} and password: {password}")
    for user in data["users"]:
        print(f"Checking against stored user: {user['name']} with password: {user['password']}")
        if user["name"] == username and user["password"] == password:
            return True
    return False

# Return balance
def get_balance(username):
    data = load_data()
    for user in data["users"]:
        if user["name"] == username:
            return user["balance"]

# Transfer money
def transfer_money(username, recipient, amount):
    data = load_data()
    sender = None
    receiver = None
    for user in data["users"]:
        if user["name"] == username:
            sender = user
        if user["name"] == recipient:
            receiver = user
    if sender and receiver and sender["balance"] >= amount:
        sender["balance"] -= amount
        receiver["balance"] += amount
        save_data(data)
        return True
    return False

# Withdraw money
def withdraw_money(username, amount):
    data = load_data()
    for user in data["users"]:
        if user["name"] == username and user["balance"] >= amount:
            user["balance"] -= amount
            save_data(data)
            return True
    return False

# Main function
def main():
    print("Welcome to the Banking System")
    
    while True:
        print("\n1. Add New User\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            login_attempts = 0
            max_login_attempts = 3
            while login_attempts < max_login_attempts:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                
                if login(username, password):
                    print("Login successful!")
                    while True:
                        print("\n1. Check Balance\n2. Transfer Money\n3. Withdraw Money\n4. Logout")
                        user_choice = input("Enter your choice: ")
                        
                        if user_choice == '1':
                            print(f"Your balance is: {get_balance(username)}")
                        
                        elif user_choice == '2':
                            transfer_attempts = 0
                            max_transfer_attempts = 3
                            while transfer_attempts < max_transfer_attempts:
                                recipient = input("Enter recipient username: ")
                                amount = float(input("Enter amount to transfer: "))
                                if transfer_money(username, recipient, amount):
                                    print("Transfer successful!")
                                    break
                                else:
                                    transfer_attempts += 1
                                    print(f"Transfer failed! Attempts left: {max_transfer_attempts - transfer_attempts}")
                            
                            if transfer_attempts == max_transfer_attempts:
                                print("Maximum transfer attempts exceeded.")
                        
                        elif user_choice == '3':
                            amount = float(input("Enter amount to withdraw: "))
                            if withdraw_money(username, amount):
                                print("Withdrawal successful!")
                            else:
                                print("Withdrawal failed!")
                        
                        elif user_choice == '4':
                            print("Logging out.")
                            break
                        
                        else:
                            print("Invalid choice!")
                    break
                else:
                    login_attempts += 1
                    print(f"Login failed! Attempts left: {max_login_attempts - login_attempts}")
            
            if login_attempts == max_login_attempts:
                print("Maximum login attempts exceeded. Exiting.")
        
        elif choice == '3':
            print("Exiting.")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()