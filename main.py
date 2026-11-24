#
#

import shifts
import reports

#----------------------------------------------
# Displays the menu options.
#----------------------------------------------

def show_menu():
    print("\n========== SHIFT PREDICTOR ==========")
    print("1. Record a Shift")
    print("2. View Shift History")
    print("3. View Transactions")
    print("4. Shift Report")
    print("5. Predict Shift Busyness")
    print("6. Estimate Tips")
    print("7. Run Customer Simulation")
    print("8. View Charts")
    print("9. Save and Exit")


#----------------------------------------------
# Loads the CSV files when the program starts.
#----------------------------------------------

shift_data = shifts.load_shifts()
transactions = shifts.load_transactions()


#----------------------------------------------
# Menu that stays open until the user chooses to exit.
#----------------------------------------------
while True:
    show_menu()
    choice = input("Please choose an option (1-9): ")

    if choice == "1":
        shifts.record_shift(shift_data, transactions)

    elif choice == "2":
        shifts.view_shifts(shift_data)

    elif choice == "3":
        shifts.view_transactions(transactions)

    elif choice == "4":
        reports.shift_report(transactions)

    elif choice in ["5", "6", "7"]:
        print("Coming soon!")

    elif choice == "8":
        reports.create_charts(transactions)

    elif choice == "9":
        shifts.save_shifts(shift_data)
        shifts.save_transactions(transactions)

        print("Your shift history and transactions have been saved!")
        print("Thank you for using the Busy Shift Predictor!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-9.")

