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


