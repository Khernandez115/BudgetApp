
def main():
    print(f"🎯 Running Expense Tracker!")
    
    # Get user input for expense
    get_user_expense()
    # Write their expense to a file.
    save_expense_to_file()
    # Read file and summarize expenses
    summarize_expenses()
    

def get_user_expense():
    print(f"🎯 Getting User Expense!")
    expense_name = input("Enter Expense name: ")
    print(f"You've entered {expense_name}")

   

def save_expense_to_file():
    print(f"🎯 Saving Expense to File!")

    
  

def summarize_expenses():
    print(f"🎯 Summarizing Expenses!")

    
   



if __name__ == "__main__":
    main()