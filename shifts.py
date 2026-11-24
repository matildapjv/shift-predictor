#--------------------------------------------------------
#
#
#
#--------------------------------------------------------

# shifts.py
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
# Loads the transaction list from its CSV file.
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
                    "total_sales": float(row["total_sales"])
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
# Displays every recorded shift in the dictionary.
#----------------------------------------------
def view_shifts(shifts):
    print("========== SHIFT HISTORY ==========")

    if len(shifts) == 0:
        print("No shifts have been recorded yet.")
    else:
        for date, data in shifts.items():
            print("Date:", date)
            print("Season:", data["season"])
            print("Day:", data["day"])
            print("Customers:", data["customers"])
            print(f"Total Sales: ${data['total_sales']:.2f}")
            print("-----------------------------")

#----------------------------------------------
# Displays every individual transaction.
#----------------------------------------------

def view_transactions(transactions):
    print("========== TRANSACTION HISTORY ==========")

    if len(transactions) == 0:
        print("No transactions recorded yet.")
    else:
        for transaction in transactions:
            print("Date:", transaction["date"])
            print("Season:", transaction["season"])
            print("Day:", transaction["day"])
            print("Customers:", transaction["customers"])
            print(f"Total Sales: ${transaction['total_sales']:.2f}")
            print("-----------------------------")

#----------------------------------------------
# Valid whole number from user.
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
# Valid money amount from user.
#----------------------------------------------

def get_float(message):
    while True:
        try:
            number = float(input(message))

            if number >= 0:
                return number
            else:
                print("Please enter an amount that is not negative.")

        except ValueError:
            print("Invalid input. Please enter a number.")

#----------------------------------------------
# Valid season from user.
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
# Valid day of the week from user.
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
# Records a shift as a transaction and updates the shift dictionary.
#----------------------------------------------

def record_shift(shifts, transactions):
    print("========== RECORD SHIFT ==========")

    date = input("Enter the shift date (YYYY-MM-DD): ")

    while date.strip() == "":
        print("The date cannot be blank.")
        date = input("Enter the shift date (YYYY-MM-DD): ")

    season = get_season()
    day = get_day()
    customers = get_integer("Enter the number of customers: ")
    total_sales = get_float("Enter the total sales for the shift: $")

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
