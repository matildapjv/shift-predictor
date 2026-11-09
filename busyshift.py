#
#
#
#
#


# example shifts

shifts = {
    "2026-07-18": {
        "season": "Summer",
        "day": "Tuesday",
        "customers": 120,
        "total_sales": 1500.00,
    },
"2026-07-19": {
        "season": "Summer",
        "day": "Wednesday",
        "customers": 80,
        "total_sales": 1000.00,
    },
"2026-07-20": {
        "season": "Summer",
        "day": "Thursday",
        "customers": 90,
        "total_sales": 1200.00,
    },
}

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
def view_shifts():
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
while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        record_shift()

    elif choice == '2':
        view_shifts()

    elif choice in ['3', '4', '5','6']:
        print(f"Coming soon!")   
         
    elif choice == "7":
        print("Exiting... Thank you for using Shift Predictor!")
        break
        
    else:
        print("Invalid choice. Please enter a number from 1-6.")


