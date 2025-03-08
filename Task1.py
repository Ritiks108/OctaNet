import time

# Simulating card insertion
print("Please enter your card")
time.sleep(4)

# Setting default ATM PIN and balance
password = 9803  # Predefined PIN (should be securely stored in real-world scenarios)
pin = int(input("Enter your atm pin: "))
balance = 6000 # Initial balance
transaction_history=[] # List to store transaction records

# Verifying user PIN
if pin == password:
    while True:
        # Displaying ATM menu options
        print("""
            1 - Balance inquiry
            2 - Withdraw
            3 - Deposit
            4 - Change Pin
            5 - Transaction history
            6 - Exit  
            """)
        try: 
            option = int(input("Please enter your choice: ")) # Taking user input
        except :
            print("Please enter a valid choice")
        # Option 1: Display current balance
        if option == 1:
            print(f"Your current balance is: {balance}")
        # Option 2: Withdraw money
        elif option == 2:
            Withdraw_Amount = int(input("Please enter your amount: "))
            if Withdraw_Amount > balance:
                print("Insufficient balance")
            else:
                balance = balance - Withdraw_Amount
                transaction_history.append(f"withdrawn: ${Withdraw_Amount}")
                print(f"Your updated balance is: {balance}")
        # Option 3: Deposit money    
        elif option == 3:
            Deposit_Amount = int(input("Please enter your amount: "))
            balance = balance + Deposit_Amount
            transaction_history.append(f"Deposited: ${Deposit_Amount}")
            print(f"Your updated balance is: {balance}")
        # Option 4: Change ATM PIN
        elif option == 4:
            New_pin = int(input("Please enter your new pin: "))
            password = New_pin
            print("PIN Changed Successfully.")
        # Option 5: Display transaction history
        elif option == 5:
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transaction yet.")
        # Option 6: Exit ATM
        elif option==6:
            print("Thank you for using the ATM. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

else:
    print("Wrong PIN entered! Please try again")
