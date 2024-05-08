import pandas as pd
import csv

class Expense_Tracker:
    def __init__(self):
        self.expenses = [] #empty list

    def add_expense(self, date, category, amount):
        self.expenses.append({'Date': date, 'Category': category, 'Amount': amount}) #appends dict, keys:date,category,amount
        print("Expense added successfully")

    def view_expenses(self):
        a = pd.DataFrame(self.expenses) #takes list & create dataframe,
        print("All Expenses:")
        print(a)

    def analyse_expenses(self):
        b = pd.DataFrame(self.expenses) #
        analysis = b.groupby('Category')['Amount'].sum() #groups data in 'b' based on category,it make all rows together with same category
        print("Expense Analysis:")
        print(analysis)

    def save_expenses(self, filename):
        c = pd.DataFrame(self.expenses)
        c.to_csv(filename, index=False) #saves dataframe to CSV file, index=False :the index from dataframe is not saved in csv file
        print("Expenses saved successfully to", filename)

    def load_expenses(self, filename):
            d = pd.read_csv(filename) #read data from csv file
            self.expenses = d.to_dict('records') #to_dict :converts dataframe into list of dict's, records represents row
            print("Expenses loaded successfully from", filename)
        

def main():
    expense_tracker = Expense_Tracker() #instance
    
    print("Welcome to the Expense Tracker!")
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Analyze Expenses\n4. Save Expenses\n5. Load Expenses\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print('Enter expense details: ')
            date = input("date (YYYY-MM-DD): ")
            category = input("category: ")
            amount = float(input("amount: "))
            expense_tracker.add_expense(date, category, amount)

        elif choice == '2':
            expense_tracker.view_expenses()

        elif choice == '3':
            expense_tracker.analyse_expenses()

        elif choice == '4':
            filename = input("Enter filename to save expenses: ")
            expense_tracker.save_expenses(filename)

        elif choice == '5':
            filename = input("Enter filename to load expenses: ")
            expense_tracker.load_expenses(filename)

        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            exit(0)


if __name__ == "__main__":
    main()
