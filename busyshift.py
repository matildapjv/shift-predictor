#
#
#
#
# also incprperate if its raining, cloudy, sunny, or snowing.


import csv

# Loads the shift dictionary from the CSV file.
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

# Saves the shift dictionary to the CSV file.
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

## show the menu options 

def show_menu():
    print("========== Shift Predictor =========")
    print("1. Predict Shift Busyness")
    print("2. View Shift History")
    print("3. Record shift History")
    print("4. Run Customer Simulation")
    print("5. Run Gratuity Simulation")
    print("6. View Charts")
    print("7. Exit")    

# display every recorded shift and its information
def view_shifts(shifts):
    print("========== Shift History =========")
    for date, data in shifts.items():
        print(f"Date: {date}")
        print(f"Season: {data['season']}")
        print(f"Day: {data['day']}")
        print(f"Customers: {data['customers']}")
        print(f"Total Sales: ${data['total_sales']:.2f}")
        print("-----------------------------")

# get a whole number from user

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


# get valid money input from user
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

# update shift or add new shift
def record_shift():
    print("========== Record Shift =========")
   
    date = input("Enter the date of the shift (YYYY-MM-DD): ")

    if date in shifts:
        print("This shift already exists. Updating shift information:")
    else:
        print("Adding new shift!")

        season = input("Enter the season (Spring, Summer, Fall, Winter): ")
        day = input("Enter the day of the week: ")

        customers = get_integer("Enter the number of customers: ")
        total_sales = get_float("Enter the total sales amount: ")

        shifts[date] = {
            "season": season,
            "day": day,
            "customers": customers,
            "total_sales": total_sales
        }

# menu that stays open until the user chooses to exit
shifts = load_shifts()

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        record_shift()

    elif choice == '2':
        view_shifts(shifts)

    elif choice in ['3', '4', '5','6']:
        print(f"Coming soon!")   
         
    elif choice == "7":
        print("Exiting... Thank you for using Shift Predictor!")
        break
        
    else:
        print("Invalid choice. Please enter a number from 1-6.")


