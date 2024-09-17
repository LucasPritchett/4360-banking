#4369-banking 

#User-friendly banking

1. **Add New User**
   - Run the program.
   - Select option `1` to add a new user.
   - Enter the new user's name, password, and initial balance.
   - The new user will be added to the `bank_data.json` file.

2. **Login**
   - Run the program.
   - Select option `2` to log in.
   - Enter your username and password.
   - If the login is successful, you will be able to perform various actions such as checking balance, transferring money, and withdrawing money.
   - If the login fails, you will have up to 3 attempts to log in successfully.

3. **Check Balance**
   - After logging in, select option `1` to check your balance.
   - The program will display your current balance.

4. **Transfer Money**
   - After logging in, select option `2` to transfer money.
   - Enter the recipient's username and the amount to transfer.
   - You will have up to 3 attempts to transfer money successfully.

5. **Withdraw Money**
   - After logging in, select option `3` to withdraw money.
   - Enter the amount to withdraw.
   - The program will display a success or failure message based on the transaction.

6. **Logout**
   - After logging in, select option `4` to log out.
   - The program will return to the main menu.

7. **Exit**
   - Select option `3` from the main menu to exit the program.

### Functional Requirements

1. **User Authentication**
   - Users must log in with a username and password.
   - Limit login attempts to 3.

2. **Account Management**
   - Return the current balance.
   - Transfer money to another account.
   - Withdraw money from the account.
   - Limit transfer attempts to 3.

Non-Functional Requirements

1. **Security**
   - Passwords are stored in plain text for simplicity.

2. **Usability**
   - The interface should be user-friendly.
   - Provide clear error messages and feedback.

3. **Performance**
   - The system should handle multiple users efficiently.
   - Ensure quick response times for transactions.

Design Constraints

#Uses Python for the backend logic.
#The interface is a simple command-line interface.
#Uses a simple file-based storage for user data and account balances.
