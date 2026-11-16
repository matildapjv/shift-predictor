#
#

import csv
#----------------------------------------------
# Loads the shift dictionary from the CSV file.
#----------------------------------------------
def load_shifts():
    shifts = {}

    try:
        with open("shifts.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                shifts[row["date"]] = {
                    "season": row["season"],
                    "day": row["day"],
                    "customers": int(row["customers"]),
                    "total_sales": float(row["total_sales"])
                }

    except FileNotFoundError:
        print("No shift file found. Starting with an empty shift history.")

    return shifts

#----------------------------------------------
# Saves the shift dictionary to the CSV file.
#----------------------------------------------

def save_shifts(shifts):
    with open("shifts.csv", "w", newline="") as file:
        fieldnames = ["date", "season", "day", "customers", "total_sales"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for date, details in shifts.items():
            writer.writerow({
                "date": date,
                "season": details["season"],
                "day": details["day"],
                "customers": details["customers"],
                "total_sales": details["total_sales"]
            })

#----------------------------------------------
# Loads rhe transaction list from its CSV file
#----------------------------------------------
def load_transactions():
    transactions = []

    try:
        with open("transactions.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                transactions.append({
                    "date": row["date"],
                    "season": row["season"],
                    "day": row["day"],
                    "customers": int(row["customers"]),
                    "total_sales": float(row["total_sales"]),
                })

    except FileNotFoundError:
        print("No transaction file found. Starting with an empty transaction history.")

    return transactions

#----------------------------------------------
# Saves the transaction list to its CSV file.
#----------------------------------------------

def save_transactions(transactions):
    with open("transactions.csv", "w", newline="") as file:
        fieldnames = ["date", "season", "day", "customers", "total_sales"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for transaction in transactions:
            writer.writerow(transaction)

#----------------------------------------------
# show the menu options 
#----------------------------------------------

def show_menu():
    print("========== Shift Predictor =========")
    print("1. Record a Shift")
    print("2. View Shift History")
    print("3. View Transactions")
    print("4. Predict Shift Busyness")
    print("5. Estimate Tips")
    print("6. Run Customer Simulation")
    print("7. View Charts")
    print("8. Save and Exit")    

#----------------------------------------------
# display every recorded shift in the dictionary
#----------------------------------------------
def view_shifts(shifts):
    print("========== Shift History =========")
    for date, data in shifts.items():
        print(f"Date: {date}")
        print(f"Season: {data['season']}")
        print(f"Day: {data['day']}")
        print(f"Customers: {data['customers']}")
        print(f"Total Sales: ${data['total_sales']:.2f}")
        print("-----------------------------")

#----------------------------------------------
#Display every recorded transaction in the list
#----------------------------------------------

def view_transactions(transactions):
    print("========== Transaction History =========")

    if len(transactions) == 0:
        print("No transactions recorded yet.")
    else:
        for transaction in transactions:
            print(f"Date: {transaction['date']}")
            print(f"Season: {transaction['season']}")
            print(f"Day: {transaction['day']}")
            print(f"Customers: {transaction['customers']}")
            print(f"Total Sales: ${transaction['total_sales']:.2f}")
            print("-----------------------------")

#----------------------------------------------
# get a whole number from user
#----------------------------------------------

def get_integer(message):
    while True:
        try:
            number = int(input(message))

            if number >= 0:
                return number
            else:
                print("Please enter a number that is not negative.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

#----------------------------------------------
#  valid money input
#----------------------------------------------

def get_float(prompt):
    while True:
        try:
            number = float(input(prompt))

            if number >= 0:
                return number
            else:
                print("Please enter an amount that is not negative.")

        except ValueError:
            print("Invalid input. Please enter a number.")

#----------------------------------------------
# valid season input
#----------------------------------------------
def get_season():
    while True:
        season = input("Enter the season (Spring, Summer, Fall, Winter): ")
        season = season.capitalize()

        if season in ["Spring", "Summer", "Fall", "Winter"]:
            return season
        else:
            print("Invalid season. Please enter Spring, Summer, Fall, or Winter.")

#----------------------------------------------
# valid day input
#----------------------------------------------
def get_day():
    while True:
        day = input("Enter the day of the week: ")
        day = day.capitalize()

        if day in ["Monday", "Tuesday", "Wednesday", "Thursday",
                   "Friday", "Saturday", "Sunday"]:
            return day
        else:
            print("Invalid day. Please enter a day of the week.")

#----------------------------------------------
# record a shift as a transaction and updates the shift dictionary
#----------------------------------------------

def record_shift():
    print("========== Record Shift =========")
   
    date = input("Enter the shift date (YYYY-MM-DD): ")

    while date.strip() == "":
        print("The date cannot be blank.")
        date = input("Enter the shift date (YYYY-MM-DD): ")

    season = get_season()
    day = get_day()
    customers = get_integer("Enter the number of customers: ")
    total_sales = get_float("Enter the total sales: $")

    transaction = {
        "date": date,
        "season": season,
        "day": day,
        "customers": customers,
        "total_sales": total_sales
    }

    transactions.append(transaction)

    shifts[date] = {
        "season": season,
        "day": day,
        "customers": customers,
        "total_sales": total_sales
    }

    print("Shift transaction recorded successfully!")

#----------------------------------------------
#loads both of the CSV files when the program starts
#----------------------------------------------
shifts = load_shifts()
transactions = load_transactions()

#----------------------------------------------
# menu that stays open until the user chooses to exit
#----------------------------------------------

while True:
    show_menu()
    choice = input("Please choose an option (1-8): ")

    if choice == "1":
        record_shift()
    elif choice == "2":
        view_shifts(shifts)
    elif choice == "3":
        view_transactions(transactions)
    elif choice in ["4", "5", "6", "7"]:
        print("Coming soon!")
    elif choice == "8":
        save_shifts(shifts)
        save_transactions(transactions)
        print("Your shift history and transactions have been saved!")
        print("Thank you for using the Busy Shift Predictor!")
        break
    else:
        print("Invalid choice. Please enter a number from 1-8.")

